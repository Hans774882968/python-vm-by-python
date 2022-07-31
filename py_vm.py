import operator
from typing import Union
import copy
from collections.abc import Iterable


class PyVm:
    def __init__(self, what_to_execute):
        self.stack = []
        self.env = {
            "print": "print_func",
        }
        self.what_to_execute = what_to_execute
        self.instructions = what_to_execute["co_code"]
        # 认为 self.program_counter 总是2的倍数
        self.program_counter: int = 0
        self.in_loop = 0

    def top(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def push(self, *args):
        for arg in args:
            self.stack.append(arg)

    def pop_n(self, n: int):
        if not n:
            return []
        ret = self.stack[-n:]
        self.stack[-n:] = []
        return ret

    def set_top(self, value):
        self.stack[-1] = value

    def get_const(self, index: int):
        return self.what_to_execute["co_consts"][index]

    def get_name(self, index: int):
        return self.what_to_execute["co_names"][index]

    def get_global(self, index: int):
        return self.what_to_execute["co_globals"][index]

    def parse_arg(self, instruction, arg: int) -> Union[str, int]:
        if instruction in ["LOAD_CONST"]:
            return self.get_const(arg)
        if instruction in ["LOAD_NAME", "STORE_NAME"]:
            return self.get_name(arg)
        return arg

    def load_const(self, const):
        self.push(const)

    def load_name(self, name: str):
        # 不需要深拷贝
        self.push(self.env[name])

    def store_name(self, name: str):
        # 把计算栈的值赋给运行环境的对应变量，需要深拷贝
        self.env[name] = copy.deepcopy(self.top())

    def build_tuple(self, num: int):
        arr = self.pop_n(num)
        self.push(tuple(arr))

    def build_list(self, num: int):
        arr = self.pop_n(num)
        self.push(arr)

    def build_map(self):
        self.push({})

    UNARY_OPERATORS = {
        'POSITIVE': operator.pos,  # +a
        'NEGATIVE': operator.neg,  # -a
        'NOT': operator.not_,  # not a
        'CONVERT': repr,
        'INVERT': operator.invert,  # ~a
    }

    def unary_operator(self, op: str):
        value = self.top()
        self.set_top(self.UNARY_OPERATORS[op](value))

    BINARY_OPERATORS = {
        'POWER': pow,          # a ** b
        'MULTIPLY': operator.mul,  # a * b
        'FLOOR_DIVIDE': operator.floordiv,  # a // b
        'TRUE_DIVIDE': operator.truediv,  # a / b
        'MODULO': operator.mod,           # a % b
        'ADD': operator.add,           # a + b
        'SUBTRACT': operator.sub,           # a - b
        'SUBSCR': operator.getitem,       # a[b]
        'LSHIFT': operator.lshift,        # a << b
        'RSHIFT': operator.rshift,        # a >> b
        'AND': operator.and_,          # a & b
        'XOR': operator.xor,           # a ^ b
        'OR': operator.or_,           # a | b
    }

    def binary_operator(self, op: str):
        x, y = self.pop_n(2)
        self.push(self.BINARY_OPERATORS[op](x, y))

    def inplace_operator(self, op: str):
        y = self.pop()
        x = self.top()
        self.set_top(self.BINARY_OPERATORS[op](x, y))

    # TOS1[TOS] = TOS2
    def store_subscr(self):
        val, arr, idx = self.pop_n(3)
        arr[idx] = val

    COMPARE_OPERATORS = [
        operator.lt,
        operator.le,
        operator.eq,
        operator.ne,
        operator.gt,
        operator.ge,
        lambda x, y: x in y,
        lambda x, y: x not in y,
        lambda x, y: x is y,
        lambda x, y: x is not y,
        lambda x, y: issubclass(x, Exception) and issubclass(x, y),
    ]

    def compare_op(self, op_index: int):
        y = self.pop()
        x = self.top()
        self.set_top(self.COMPARE_OPERATORS[op_index](x, y))

    # 暂时这么实现，认为要call的函数只有 print
    def call_function(self, argv: int):
        args = []
        for _ in range(argv):
            args.append(self.pop())
        args = args[::-1]
        print(*args)
        self.pop()  # 先把函数名 'print_func' 去掉，再放返回值进去
        self.push(None)  # print 函数的返回值

    def jump_absolute(self, addr: int):
        self.program_counter = addr

    def jump_forward(self, offset: int):
        self.program_counter += offset

    def pop_jump_if_false(self, addr: int) -> bool:
        value = self.pop()
        if not value:
            self.program_counter = addr
            return False
        return True

    def pop_jump_if_true(self, addr: int) -> bool:
        value = self.pop()
        if value:
            self.program_counter = addr
            return True
        return False

    def dup_top(self):
        self.push(self.top())

    def dup_top_two(self):
        a, b = self.pop_n(2)
        self.push(a, b, a, b)

    def rot_two(self):
        a, b = self.pop_n(2)
        self.push(b, a)

    def rot_three(self):
        a, b, c = self.pop_n(3)
        self.push(c, a, b)

    def rot_four(self):
        a, b, c, d = self.pop_n(4)
        self.push(d, a, b, c)

    # 此时栈顶是迭代器，成功 next() 则push，否则把迭代器 pop 掉
    def for_iter(self, offset: int):
        it = self.top()
        try:
            value = next(it)
            self.push(value)
        except StopIteration:
            self.pop()
            self.jump_forward(offset)

    # TOS = iter(TOS)，失败就pop掉
    def get_iter(self):
        value = self.top()
        value_iter = iter(value)
        if value_iter:
            self.set_top(value_iter)
        else:
            self.pop()

    def return_value(self):
        ret_value = self.pop()
        return str(ret_value)

    def run_code(self):
        while True:
            if self.program_counter // 2 >= len(self.instructions):
                break
            step = self.instructions[self.program_counter // 2]
            instruction, arg = step if len(step) > 1 else (step + (None,))
            arg = self.parse_arg(instruction, arg)

            change_pc = True
            if instruction == "LOAD_NAME":
                self.load_name(arg)
            elif instruction == "STORE_NAME":
                self.store_name(arg)
            elif instruction == "LOAD_CONST":
                self.load_const(arg)
            elif instruction == "BUILD_LIST":
                self.build_list(arg)
            elif instruction == "BUILD_TUPLE":
                self.build_tuple(arg)
            elif instruction == "BUILD_MAP":
                self.build_map()
            elif instruction.startswith("UNARY_"):
                self.binary_operator(instruction[6:])
            elif instruction.startswith("BINARY_"):
                self.binary_operator(instruction[7:])
            elif instruction.startswith("INPLACE_"):
                self.inplace_operator(instruction[8:])
            elif instruction == "STORE_SUBSCR":
                self.store_subscr()
            elif instruction == "COMPARE_OP":
                self.compare_op(arg)
            elif instruction == "CALL_FUNCTION":
                self.call_function(arg)
            elif instruction == "JUMP_ABSOLUTE":
                self.jump_absolute(arg)
                # 拿到迭代器。感觉这块非常不对。
                if self.in_loop:
                    while not isinstance(self.top(), Iterable):
                        self.pop()
                change_pc = False
            elif instruction == "JUMP_FORWARD":
                self.jump_forward(arg)
            elif instruction == "POP_JUMP_IF_FALSE":
                fl = self.pop_jump_if_false(arg)
                if not fl:
                    change_pc = False
            elif instruction == "POP_JUMP_IF_TRUE":
                fl = self.pop_jump_if_true(arg)
                if fl:
                    change_pc = False
            elif instruction == "POP_TOP":
                self.pop()
            elif instruction == "DUP_TOP":
                self.dup_top()
            elif instruction == "DUP_TOP_TWO":
                self.dup_top_two()
            elif instruction == "ROT_TWO":
                self.rot_two()
            elif instruction == "ROT_THREE":
                self.rot_three()
            elif instruction == "ROT_FOUR":
                self.rot_four()
            # 暂时没有块栈（block stack）的概念
            # 暂时用 SETUP_LOOP 表示进循环， POP_BLOCK 表示出循环
            elif instruction == "SETUP_LOOP":
                self.in_loop += 1
                print('[dbg] SETUP_LOOP ignored')  # dbg
                pass
            # 暂时没有块栈（block stack）的概念
            elif instruction == "POP_BLOCK":
                self.in_loop -= 1
                print('[dbg] POP_BLOCK ignored')  # dbg
                pass
            elif instruction == "FOR_ITER":
                self.for_iter(arg)
            elif instruction == "GET_ITER":
                self.get_iter()
            elif instruction == "RETURN_VALUE":
                self.return_value()
            else:
                raise Exception(f'Unsupported instruction: {step}')
            # change_pc = False 表示不需要 self.program_counter 增加
            if change_pc:
                self.program_counter += 2
        print('[dbg] stack', self.stack)  # dbg


if __name__ == '__main__':
    from test_cases import test_cases
    for i, test_case in enumerate(test_cases[:-1]):
        print(f'[dbg] test case {i+1}')  # dbg
        py_vm = PyVm(test_case)
        py_vm.run_code()
