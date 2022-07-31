[TOC]

这是一个python字节码练手demo，参考的代码是参考链接1。经过此demo，可以对python执行字节码所用到的栈（主要指计算栈）有非常初步的了解。

### 项目结构

1. `py_vm.py`是唯一的主文件。
2. `test_cases.py`存放测试用例。
3. `demos`文件夹用来生成测试用例。

### 支持

1. 定义变量
2. 基本的计算
3. 数组取单个元素
4. if语句
5. for循环
6. print

目前还不支持print以外的函数。

### 加入新测试用例

1. 在`demos`文件夹新建py文件。
2. 在`demos/mydis.py`修改`global_demo_paths`变量，把刚刚的py文件的相对路径加进去。并运行`demos/mydis.py`。
3. 修改`demos/parse_dis.py`的`global_demo_path`，然后运行`demos/parse_dis.py`。
4. 根据以上两步输出结果修改`test_cases.py`。

### 参考链接

1. 参考的代码：https://github.com/VxCoder/PythonVM
2. python字节码官方文档：https://docs.python.org/3.7/library/dis.html
3. python字节码可参考文档（`dis`库的使用）：https://www.docs4dev.com/docs/zh/python/3.7.2rc1/all/library-dis.html