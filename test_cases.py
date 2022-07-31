import random

test_cases = [
    # add_demo_g.py
    {
        "co_names": ["a0", "a1", "a2", "a3", "a4", "a", "print", "b0", "b1", "b"],
        "co_globals": [],
        "co_consts": [10, 20, 30, 40, 50, "wsw", "-ruo", None],
        "co_code": [
            ("LOAD_CONST", 0),
            ("STORE_NAME", 0),
            ("LOAD_CONST", 1),
            ("STORE_NAME", 1),
            ("LOAD_CONST", 2),
            ("STORE_NAME", 2),
            ("LOAD_CONST", 3),
            ("STORE_NAME", 3),
            ("LOAD_CONST", 4),
            ("STORE_NAME", 4),

            # a = a0 + a1 + a2 + a3 + a4
            ("LOAD_NAME", 0),
            ("LOAD_NAME", 1),
            ("BINARY_ADD",),
            ("LOAD_NAME", 2),
            ("BINARY_ADD",),
            ("LOAD_NAME", 3),
            ("BINARY_ADD",),
            ("LOAD_NAME", 4),
            ("BINARY_ADD",),
            ("STORE_NAME", 5),

            # a1 += a0 + a1 + a2
            ("LOAD_NAME", 1),
            ("LOAD_NAME", 0),
            ("LOAD_NAME", 1),
            ("BINARY_ADD",),
            ("LOAD_NAME", 2),
            ("BINARY_ADD",),
            ("INPLACE_ADD",),
            ("STORE_NAME", 1),

            # print(a, a0, a1, a2, a3, a4)
            ("LOAD_NAME", 6),
            ("LOAD_NAME", 5),
            ("LOAD_NAME", 0),
            ("LOAD_NAME", 1),
            ("LOAD_NAME", 2),
            ("LOAD_NAME", 3),
            ("LOAD_NAME", 4),
            ("CALL_FUNCTION", 6),
            ("POP_TOP",),

            # b0 = "wsw";b1 = " ruo";b = b0 + b1;print(b, b0, b1)
            ("LOAD_CONST", 5),
            ("STORE_NAME", 7),
            ("LOAD_CONST", 6),
            ("STORE_NAME", 8),
            ("LOAD_NAME", 7),
            ("LOAD_NAME", 8),
            ("BINARY_ADD",),
            ("STORE_NAME", 9),
            ("LOAD_NAME", 6),
            ("LOAD_NAME", 9),
            ("LOAD_NAME", 7),
            ("LOAD_NAME", 8),
            ("CALL_FUNCTION", 3),
            ("POP_TOP",),

            # 固定有一个return None
            ("LOAD_CONST", 7),
            ("RETURN_VALUE",)
        ]
    },
    # multiply_demo_g.py
    {
        "co_names": ["a0", "a1", "a2", "a3", "a4", "a", "b0", "b", "c", "print"],
        "co_globals": [],
        "co_consts": [10, 20, 30, 40, 50, "a", "b", 2, None],
        "co_code": [
            ('LOAD_CONST', 0),
            ('STORE_NAME', 0),
            ('LOAD_CONST', 1),
            ('STORE_NAME', 1),
            ('LOAD_CONST', 2),
            ('STORE_NAME', 2),
            ('LOAD_CONST', 3),
            ('STORE_NAME', 3),
            ('LOAD_CONST', 4),
            ('STORE_NAME', 4),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('LOAD_NAME', 2),
            ('BINARY_ADD',),
            ('BINARY_MULTIPLY',),
            ('LOAD_NAME', 3),
            ('LOAD_NAME', 4),
            ('BINARY_MULTIPLY',),
            ('BINARY_ADD',),
            ('STORE_NAME', 5),
            ('LOAD_CONST', 5),
            ('STORE_NAME', 0),
            ('LOAD_CONST', 6),
            ('STORE_NAME', 6),
            ('LOAD_NAME', 0),
            ('LOAD_CONST', 7),
            ('BINARY_MULTIPLY',),
            ('LOAD_NAME', 6),
            ('LOAD_CONST', 7),
            ('BINARY_MULTIPLY',),
            ('BINARY_ADD',),
            ('STORE_NAME', 7),
            ('LOAD_NAME', 7),
            ('LOAD_CONST', 7),
            ('BINARY_MULTIPLY',),
            ('STORE_NAME', 8),
            ('LOAD_NAME', 9),
            ('LOAD_NAME', 5),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 3),
            ('LOAD_NAME', 4),
            ('CALL_FUNCTION', 6),
            ('POP_TOP',),
            ('LOAD_NAME', 9),
            ('LOAD_NAME', 6),
            ('LOAD_NAME', 7),
            ('LOAD_NAME', 8),
            ('CALL_FUNCTION', 3),
            ('POP_TOP',),
            ('LOAD_CONST', 8),
            ('RETURN_VALUE',)
        ]
    },
    # if_demo_g.py
    {
        "co_names": ["grade", "print"],
        "co_globals": [],
        # 给 grade 随机一个初值
        "co_consts": [random.choice([10 * i for i in range(11)]), 60, "不及格", 90, "良好", "优秀", "结束", None],
        "co_code": [
            ('LOAD_CONST', 0),
            ('STORE_NAME', 0),
            ('LOAD_NAME', 0),
            ('LOAD_CONST', 1),
            ('COMPARE_OP', 0),
            ('POP_JUMP_IF_FALSE', 22),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 2),
            ('CALL_FUNCTION', 1),
            ('POP_TOP',),
            ('JUMP_FORWARD', 26),
            ('LOAD_NAME', 0),
            ('LOAD_CONST', 3),
            ('COMPARE_OP', 0),
            ('POP_JUMP_IF_FALSE', 40),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 4),
            ('CALL_FUNCTION', 1),
            ('POP_TOP',),
            ('JUMP_FORWARD', 8),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 5),
            ('CALL_FUNCTION', 1),
            ('POP_TOP',),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 6),
            ('CALL_FUNCTION', 1),
            ('POP_TOP',),
            ('LOAD_CONST', 7),
            ('RETURN_VALUE',)
        ]
    },
    # arr_demo_g.py
    {
        "co_names": ["arr", "i", "print", "tmp"],
        "co_globals": [],
        "co_consts": [20, 30, 40, 50, 60, 1, "<= 20", "<= 30", "> 30", None],
        "co_code": [
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 1),
            ('LOAD_CONST', 2),
            ('LOAD_CONST', 3),
            ('LOAD_CONST', 4),
            ('BUILD_LIST', 5),
            ('STORE_NAME', 0),
            ('LOAD_CONST', 5),
            ('STORE_NAME', 1),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 0),
            ('COMPARE_OP', 1),
            ('POP_JUMP_IF_FALSE', 46),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 6),
            ('CALL_FUNCTION', 2),
            ('POP_TOP',),
            ('JUMP_FORWARD', 42),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 1),
            ('COMPARE_OP', 1),
            ('POP_JUMP_IF_FALSE', 74),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 7),
            ('CALL_FUNCTION', 2),
            ('POP_TOP',),
            ('JUMP_FORWARD', 14),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 8),
            ('CALL_FUNCTION', 2),
            ('POP_TOP',),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('BINARY_SUBSCR',),
            ('STORE_NAME', 3),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('DUP_TOP_TWO',),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 0),
            ('INPLACE_ADD',),
            ('ROT_THREE',),
            ('STORE_SUBSCR',),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 3),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('BINARY_SUBSCR',),
            ('LOAD_NAME', 0),
            ('CALL_FUNCTION', 3),
            ('POP_TOP',),
            ('LOAD_CONST', 9),
            ('RETURN_VALUE',)
        ]
    },
    # for_demo0_g.py
    {
        "co_consts": (20, 30, 40, 50, '<= 30', '> 30', '结束', None),
        "co_names": ('arr', 'v', 'print'),
        "co_code": [
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 1),
            ('LOAD_CONST', 2),
            ('LOAD_CONST', 3),
            ('BUILD_LIST', 4),
            ('STORE_NAME', 0),
            ('SETUP_LOOP', 42),
            ('LOAD_NAME', 0),
            ('GET_ITER',),
            ('FOR_ITER', 34),
            ('STORE_NAME', 1),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 1),
            ('COMPARE_OP', 1),
            ('POP_JUMP_IF_FALSE', 42),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 4),
            ('CALL_FUNCTION', 2),
            ('POP_TOP',),
            ('JUMP_ABSOLUTE', 18),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 5),
            ('CALL_FUNCTION', 2),
            ('POP_TOP',),
            ('JUMP_ABSOLUTE', 18),
            ('POP_BLOCK',),
            ('LOAD_NAME', 2),
            ('LOAD_CONST', 6),
            ('CALL_FUNCTION', 1),
            ('POP_TOP',),
            ('LOAD_CONST', 7),
            ('RETURN_VALUE',)
        ]
    },
    # for_demo1_g.py
    {
        "co_consts": (3, 4, 5, 6, 7, 2, 0, 10, 1, '结束力', None),
        "co_names": ('arr0', 'arr1', 'ii', 'i', 'jj', 'j', 'print'),
        "co_code": [
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 1),
            ('LOAD_CONST', 2),
            ('LOAD_CONST', 3),
            ('LOAD_CONST', 4),
            ('BUILD_LIST', 5),
            ('STORE_NAME', 0),
            ('LOAD_CONST', 5),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 1),
            ('LOAD_CONST', 2),
            ('BUILD_LIST', 4),
            ('STORE_NAME', 1),
            ('LOAD_CONST', 6),
            ('STORE_NAME', 2),
            ('SETUP_LOOP', 98),
            ('LOAD_NAME', 0),
            ('GET_ITER',),
            ('FOR_ITER', 90),
            ('STORE_NAME', 3),
            ('LOAD_CONST', 6),
            ('STORE_NAME', 4),
            ('SETUP_LOOP', 56),
            ('LOAD_NAME', 1),
            ('GET_ITER',),
            ('FOR_ITER', 48),
            ('STORE_NAME', 5),
            ('LOAD_NAME', 6),
            ('LOAD_NAME', 3),
            ('LOAD_NAME', 5),
            ('LOAD_NAME', 3),
            ('LOAD_CONST', 7),
            ('BINARY_MULTIPLY',),
            ('LOAD_NAME', 5),
            ('BINARY_ADD',),
            ('CALL_FUNCTION', 3),
            ('POP_TOP',),
            ('LOAD_NAME', 1),
            ('LOAD_NAME', 4),
            ('DUP_TOP_TWO',),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 8),
            ('INPLACE_ADD',),
            ('ROT_THREE',),
            ('STORE_SUBSCR',),
            ('LOAD_NAME', 4),
            ('LOAD_CONST', 8),
            ('INPLACE_ADD',),
            ('STORE_NAME', 4),
            ('JUMP_ABSOLUTE', 50),
            ('POP_BLOCK',),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 2),
            ('DUP_TOP_TWO',),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 8),
            ('INPLACE_ADD',),
            ('ROT_THREE',),
            ('STORE_SUBSCR',),
            ('LOAD_NAME', 2),
            ('LOAD_CONST', 8),
            ('INPLACE_ADD',),
            ('STORE_NAME', 2),
            ('JUMP_ABSOLUTE', 36),
            ('POP_BLOCK',),
            ('LOAD_NAME', 6),
            ('LOAD_CONST', 9),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 4),
            ('CALL_FUNCTION', 3),
            ('POP_TOP',),
            ('LOAD_CONST', 10),
            ('RETURN_VALUE',)
        ]
    },
    # comprehensive_demo0_g.py
    {
        "co_consts": (0, 10, 20, 30, 40, 1, 2, 3, 4, 'w > 2', 5, 'w <= 2', '忽略', None),
        "co_names": ('i', 'arr0', 'arr1', 'v', 'j', 'w', 'print'),
        "co_code": [
            ('LOAD_CONST', 0),
            ('STORE_NAME', 0),
            ('LOAD_CONST', 1),
            ('LOAD_CONST', 2),
            ('LOAD_CONST', 3),
            ('LOAD_CONST', 4),
            ('BUILD_LIST', 4),
            ('STORE_NAME', 1),
            ('LOAD_CONST', 5),
            ('LOAD_CONST', 6),
            ('LOAD_CONST', 7),
            ('LOAD_CONST', 8),
            ('BUILD_LIST', 4),
            ('STORE_NAME', 2),
            ('SETUP_LOOP', 142),
            ('LOAD_NAME', 1),
            ('GET_ITER',),
            ('FOR_ITER', 134),
            ('STORE_NAME', 3),
            ('LOAD_NAME', 3),
            ('LOAD_CONST', 2),
            ('COMPARE_OP', 4),
            ('POP_JUMP_IF_FALSE', 136),
            ('LOAD_CONST', 0),
            ('STORE_NAME', 4),
            ('SETUP_LOOP', 92),
            ('LOAD_NAME', 2),
            ('GET_ITER',),
            ('FOR_ITER', 74),
            ('STORE_NAME', 5),
            ('LOAD_NAME', 5),
            ('LOAD_CONST', 6),
            ('COMPARE_OP', 4),
            ('POP_JUMP_IF_FALSE', 88),
            ('LOAD_NAME', 6),
            ('LOAD_CONST', 9),
            ('LOAD_NAME', 3),
            ('LOAD_CONST', 10),
            ('BINARY_MULTIPLY',),
            ('LOAD_NAME', 5),
            ('BINARY_ADD',),
            ('CALL_FUNCTION', 2),
            ('POP_TOP',),
            ('JUMP_FORWARD', 18),
            ('LOAD_NAME', 6),
            ('LOAD_CONST', 11),
            ('LOAD_NAME', 3),
            ('LOAD_CONST', 10),
            ('BINARY_MULTIPLY',),
            ('LOAD_NAME', 5),
            ('BINARY_ADD',),
            ('CALL_FUNCTION', 2),
            ('POP_TOP',),
            ('LOAD_NAME', 2),
            ('LOAD_NAME', 4),
            ('DUP_TOP_TWO',),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 5),
            ('INPLACE_ADD',),
            ('ROT_THREE',),
            ('STORE_SUBSCR',),
            ('LOAD_NAME', 4),
            ('LOAD_CONST', 5),
            ('INPLACE_ADD',),
            ('STORE_NAME', 4),
            ('JUMP_ABSOLUTE', 56),
            ('POP_BLOCK',),
            ('JUMP_FORWARD', 8),
            ('LOAD_NAME', 6),
            ('LOAD_CONST', 12),
            ('CALL_FUNCTION', 1),
            ('POP_TOP',),
            ('LOAD_NAME', 1),
            ('LOAD_NAME', 0),
            ('DUP_TOP_TWO',),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 1),
            ('INPLACE_ADD',),
            ('ROT_THREE',),
            ('STORE_SUBSCR',),
            ('LOAD_NAME', 0),
            ('LOAD_CONST', 5),
            ('INPLACE_ADD',),
            ('STORE_NAME', 0),
            ('JUMP_ABSOLUTE', 34),
            ('POP_BLOCK',),
            ('LOAD_NAME', 6),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 1),
            ('LOAD_NAME', 2),
            ('CALL_FUNCTION', 3),
            ('POP_TOP',),
            ('LOAD_CONST', 13),
            ('RETURN_VALUE',)
        ]
    },
    # comprehensive_demo1_g.py
    {
        "co_consts": (0, 1, 2, 3, 4, 5, 6, 7, None),
        "co_names": ('c', 'arr0', 'i', 'j', 'print'),
        "co_code": [
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('BUILD_LIST', 8),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('BUILD_LIST', 8),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('BUILD_LIST', 8),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('BUILD_LIST', 8),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('BUILD_LIST', 8),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('BUILD_LIST', 8),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('BUILD_LIST', 8),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 0),
            ('BUILD_LIST', 8),
            ('BUILD_LIST', 8),
            ('STORE_NAME', 0),
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 1),
            ('LOAD_CONST', 2),
            ('LOAD_CONST', 3),
            ('LOAD_CONST', 4),
            ('LOAD_CONST', 5),
            ('LOAD_CONST', 6),
            ('LOAD_CONST', 7),
            ('BUILD_LIST', 8),
            ('STORE_NAME', 1),
            ('SETUP_LOOP', 88),
            ('LOAD_NAME', 1),
            ('GET_ITER',),
            ('FOR_ITER', 80),
            ('STORE_NAME', 2),
            ('SETUP_LOOP', 74),
            ('LOAD_NAME', 1),
            ('GET_ITER',),
            ('FOR_ITER', 66),
            ('STORE_NAME', 3),
            ('LOAD_NAME', 3),
            ('POP_JUMP_IF_TRUE', 206),
            ('LOAD_CONST', 1),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 2),
            ('BINARY_SUBSCR',),
            ('LOAD_NAME', 3),
            ('STORE_SUBSCR',),
            ('JUMP_ABSOLUTE', 184),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 2),
            ('LOAD_CONST', 1),
            ('BINARY_SUBTRACT',),
            ('BINARY_SUBSCR',),
            ('LOAD_NAME', 3),
            ('BINARY_SUBSCR',),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 2),
            ('LOAD_CONST', 1),
            ('BINARY_SUBTRACT',),
            ('BINARY_SUBSCR',),
            ('LOAD_NAME', 3),
            ('LOAD_CONST', 1),
            ('BINARY_SUBTRACT',),
            ('BINARY_SUBSCR',),
            ('BINARY_ADD',),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 2),
            ('BINARY_SUBSCR',),
            ('LOAD_NAME', 3),
            ('STORE_SUBSCR',),
            ('JUMP_ABSOLUTE', 184),
            ('POP_BLOCK',),
            ('JUMP_ABSOLUTE', 174),
            ('POP_BLOCK',),
            ('LOAD_NAME', 4),
            ('LOAD_NAME', 0),
            ('CALL_FUNCTION', 1),
            ('POP_TOP',),
            ('LOAD_CONST', 8),
            ('RETURN_VALUE',)
        ]
    },
    # for_demo0_g.py：因为有range函数，未解决。前面的几个样例均正确。
    {
        "co_consts": (115, 99, 117, 116, 102, 123, 80, 121, 104, 48, 110, 95, 66, 105, 97, 114, 67, 111, 100, 51, 125, 26, 2, 'enc =', None),
        "co_names": ('arr', 'range', 'i', 'print'),
        "co_code": [
            ('LOAD_CONST', 0),
            ('LOAD_CONST', 1),
            ('LOAD_CONST', 2),
            ('LOAD_CONST', 1),
            ('LOAD_CONST', 3),
            ('LOAD_CONST', 4),
            ('LOAD_CONST', 5),
            ('LOAD_CONST', 6),
            ('LOAD_CONST', 7),
            ('LOAD_CONST', 3),
            ('LOAD_CONST', 8),
            ('LOAD_CONST', 9),
            ('LOAD_CONST', 10),
            ('LOAD_CONST', 11),
            ('LOAD_CONST', 12),
            ('LOAD_CONST', 13),
            ('LOAD_CONST', 10),
            ('LOAD_CONST', 14),
            ('LOAD_CONST', 15),
            ('LOAD_CONST', 7),
            ('LOAD_CONST', 11),
            ('LOAD_CONST', 16),
            ('LOAD_CONST', 17),
            ('LOAD_CONST', 18),
            ('LOAD_CONST', 19),
            ('LOAD_CONST', 20),
            ('BUILD_LIST', 26),
            ('STORE_NAME', 0),
            ('SETUP_LOOP', 32),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 21),
            ('CALL_FUNCTION', 1),
            ('GET_ITER',),
            ('FOR_ITER', 20),
            ('STORE_NAME', 2),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 2),
            ('DUP_TOP_TWO',),
            ('BINARY_SUBSCR',),
            ('LOAD_NAME', 2),
            ('INPLACE_ADD',),
            ('ROT_THREE',),
            ('STORE_SUBSCR',),
            ('JUMP_ABSOLUTE', 66),
            ('POP_BLOCK',),
            ('SETUP_LOOP', 36),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 21),
            ('CALL_FUNCTION', 1),
            ('GET_ITER',),
            ('FOR_ITER', 24),
            ('STORE_NAME', 2),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 2),
            ('DUP_TOP_TWO',),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 21),
            ('LOAD_NAME', 2),
            ('BINARY_SUBTRACT',),
            ('INPLACE_XOR',),
            ('ROT_THREE',),
            ('STORE_SUBSCR',),
            ('JUMP_ABSOLUTE', 100),
            ('POP_BLOCK',),
            ('SETUP_LOOP', 36),
            ('LOAD_NAME', 1),
            ('LOAD_CONST', 21),
            ('CALL_FUNCTION', 1),
            ('GET_ITER',),
            ('FOR_ITER', 24),
            ('STORE_NAME', 2),
            ('LOAD_NAME', 0),
            ('LOAD_NAME', 2),
            ('DUP_TOP_TWO',),
            ('BINARY_SUBSCR',),
            ('LOAD_CONST', 22),
            ('LOAD_NAME', 2),
            ('BINARY_MULTIPLY',),
            ('INPLACE_MULTIPLY',),
            ('ROT_THREE',),
            ('STORE_SUBSCR',),
            ('JUMP_ABSOLUTE', 138),
            ('POP_BLOCK',),
            ('LOAD_NAME', 3),
            ('LOAD_CONST', 23),
            ('LOAD_NAME', 0),
            ('CALL_FUNCTION', 2),
            ('POP_TOP',),
            ('LOAD_CONST', 24),
            ('RETURN_VALUE',)
        ]
    }
]
# case1
# 150 10 80 30 40 50
# wsw-ruo wsw -ruo
# [dbg] stack [10, 20, 30, 40, 50, 150, 80, 'wsw', '-ruo', 'wsw-ruo']

# case2
# 2500 a 20 30 40 50
# b aabb aabbaabb
# [dbg] stack [10, 20, 30, 40, 50, 2500, 'a', 'b', 'aabb', 'aabbaabb']

# case3
# 不及格
# 结束
# [dbg] stack [20]

# case4
# 30 <= 30
# 30 50 [20, 50, 40, 50, 60]
# [dbg] stack [[20, 30, 40, 50, 60], 1, 30]

# case5
# [dbg] SETUP_LOOP ignored
# 20 <= 30
# 30 <= 30
# 40 > 30
# 50 > 30
# [dbg] POP_BLOCK ignored
# 结束
# [dbg] stack [[20, 30, 40, 50]]

# case6
# [dbg] SETUP_LOOP ignored
# [dbg] SETUP_LOOP ignored
# 3 2 32
# 3 3 33
# 3 4 34
# 3 5 35
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# 4 3 43
# 4 4 44
# 4 5 45
# 4 6 46
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# 5 4 54
# 5 5 55
# 5 6 56
# 5 7 57
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# 6 5 65
# 6 6 66
# 6 7 67
# 6 8 68
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# 7 6 76
# 7 7 77
# 7 8 78
# 7 9 79
# [dbg] POP_BLOCK ignored
# [dbg] POP_BLOCK ignored
# 结束力 5 4
# [dbg] stack [[3, 4, 5, 6, 7], [2, 3, 4, 5], 0]

# case7
# [dbg] SETUP_LOOP ignored
# 忽略
# 忽略
# [dbg] SETUP_LOOP ignored
# w <= 2 151
# w <= 2 152
# w > 2 153
# w > 2 154
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# w <= 2 202
# w > 2 203
# w > 2 204
# w > 2 205
# [dbg] POP_BLOCK ignored
# [dbg] POP_BLOCK ignored
# 4 [20, 30, 40, 50] [3, 4, 5, 6]
# [dbg] stack [0, [10, 20, 30, 40], [1, 2, 3, 4]]

# case8
# [dbg] SETUP_LOOP ignored
# [dbg] SETUP_LOOP ignored
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# [dbg] POP_BLOCK ignored
# [dbg] SETUP_LOOP ignored
# [dbg] POP_BLOCK ignored
# [dbg] POP_BLOCK ignored
# [[1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0, 0], [1, 3, 3, 1, 0, 0, 0, 0], [1, 4, 6, 4, 1, 0, 0, 0], [1, 5, 10, 10, 5, 1, 0, 0], [1, 6, 15, 20, 15, 6, 1, 0], [1, 7, 21, 35, 35, 21, 7, 1]]
# [dbg] stack [[[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]], [0, 1, 2, 3, 4, 5, 6, 7]]
