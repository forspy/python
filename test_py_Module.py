# 1.模块就是程序[重要]
# 2.任何python程序都可以作为模块导入
import math

print(math.sin(0))

import sys  # 添加模块路径

sys.path.append('E:\\python code\\test_py_hello')  # 注意：string里面双斜杠才表示\
import test_py_hello
# 3.模块一般只导入一次
# 4.模块被用于下定义
# 5.模块有着自己的作用域，如果定义在全局的模块可以反复使用其函数进行代码重用

import test_py_hello2

test_py_hello2.hello()  # 可以使用模块中定义的函数或者变量 [重要]
print(test_py_hello2.A)

import test_py_hello3

test_py_hello3.hello()
# #如果只想使用程序中的函数或者变量而不想执行整个程序，就可以导入测试模块
# def hello():
#     print('hello world')
#
# if __name__=='__main__':hello() #测试模块，在本程序中能够运行，在模块程序中不会主动运行

import sys, pprint

print(pprint.pprint(sys.path))  # 通过这种方法可以看到python加载的文件路径
# 一般来说D:\\test_py_Module\\lib\\site-packages 放到这下面是一个不错的选择 只要放在这下面就能自动导入模块
import test  # 当然放在当前项目下也是一个不错的选择

# 环境变量是操作系统的一部分 表示去哪里能找到python这个解释器

# python使用包 ，包就是模块的集合，是一个文件夹
# 包必须包含__init__.py文件
import test_py_constant  # 导入整个包

print(test_py_constant.PI)  # 使用包中某一.py模块文件的变量 [重要]python的导包机制非常强大 需要好好使用这个功能

from test_py_constant import shapes  # 从包中导入指定的模块

print(shapes.e)  # 使用模块中的变量

# 使用dir来查看模块中包含哪些
print(dir(test_py_hello))
# 可以看到包含了['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

# 看看模块中具体那一部分
print(test_py_hello.__cached__)  # E:\python code\test_py_hello\__pycache__\test_py_hello.cpython-37.pyc
# print(test_py_hello.__builtins__)#版本
print(test_py_hello.__file__)  # 路径E:\python code\test_py_hello\test_py_hello.py
print(test_py_hello.__loader__)  # <_frozen_importlib_external.SourceFileLoader object at 0x00000168120CCB00>
print(test_py_hello.__name__)  # test_py_hello

print(dir(
    test_py_constant))  # ['PI', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'shapes']
# 对于包来说，可以看到下面的所有模块

print(help(test_py_constant.shapes))  # 推荐使用help查看某一某块的相关参数
print(print.__doc__)  # __doc__就是对于函数的说明

