import dis
from add_demo import *
from multiply_demo import *
from if_demo import *

with open('demos/add_demo.txt', 'w', encoding='utf-8') as f:
    dis.dis(add_demo, file=f)
with open('demos/multiply_demo.txt', 'w', encoding='utf-8') as f:
    dis.dis(multiply_demo, file=f)
with open('demos/if_demo.txt', 'w', encoding='utf-8') as f:
    dis.dis(if_demo, file=f)

global_demo_paths = [
    'demos/add_demo_g',
    'demos/multiply_demo_g',
    'demos/if_demo_g',
    'demos/arr_demo_g',
    'demos/for_demo_g',
    'demos/for_demo0_g',
    'demos/for_demo1_g',
    'demos/comprehensive_demo0_g'
]
for global_demo_path in global_demo_paths:
    with open(f'{global_demo_path}.txt', 'w', encoding='utf-8') as f:
        f_path = f'{global_demo_path}.py'
        with open(f_path, 'r', encoding='utf-8') as py_f:
            code = compile(py_f.read(), f_path, 'exec')
            f.write(f'co_consts = {code.co_consts}\n')
            f.write(f'co_names = {code.co_names}\n')
            dis.dis(code, file=f)
