# 每个异常都是某个类
# 要引发一个异常，可以使用raise语句 相当于c++里面的throw
# raise Exception  # 可以是Exception，也可以是Exception的派生类
try:  # 事实上可以使用try来让程序跳过报错阶段
    raise Exception('hello')  # 可添加错误消息
except:
    pass
# 一些常见内置的异常类
# BaseException:所有异常的基类,包括退出异常和非退出异常；
# SystemExit: 解释器请求退出
# KeyboardInterrupt: 用户中断执行(通常是输入^C)
# Exception: 常规错误的基类
# StopIteration: 迭代器没有更多的值
# GeneratorExit: 生成器(generator)发生异常来通知退出
# ArithmeticError: 所有数值计算错误的基类
# FloatingPointError: 浮点计算错误
# OverflowError: 数值运算超出最大限制
# ZeroDivisionError: 除(或取模)零 (所有数据类型)
# AssertionError: 断言语句失败
# AttributeError: 对象没有这个属性
# EOFError: 没有内建输入,到达EOF标记
# EnvironmentError: 操作系统错误的基类
# IOError: 输入/输出操作失败
# OSError: 操作系统错误
# WindowsError: 系统调用失败
# ImportError: 导入模块/对象失败
# LookupError: 无效数据查询的基类
# IndexError: 序列中没有此索引(index)
# KeyError: 映射中没有这个键
# MemoryError: 内存溢出错误(对于Python 解释器不是致命的)
# NameError: 未声明/初始化对象 (没有属性)
# UnboundLocalError: 访问未初始化的本地变量
# ReferenceError: 弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError: 一般的运行时错误
# NotImplementedError: 尚未实现的方法
# SyntaxError: Python语法错误
# IndentationError: 缩进错误
# TabError: Tab和空格混用
# SystemError: 一般的解释器系统错误
# TypeError: 对类型无效的操作
# ValueError: 传入无效的参数
# UnicodeError: Unicode相关的错误
# UnicodeDecodeError: Unicode解码时的错误
# UnicodeEncodeError: Unicode编码时错误
# UnicodeTranslateError: Unicode转换时错误
# Warning: 警告的基类
# DeprecationWarning: 关于被弃用的特征的警告
# FutureWarning: 关于构造将来语义会有改变的警告
# OverflowWarning: 旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarning: 关于特性将会被废弃的警告
# RuntimeWarning: 可疑的运行时行为(runtime behavior)的警告
# SyntaxWarning: 可疑的语法的警告
# UserWarning: 用户代码生成的警告

# 捕获异常 c++使用try catch

try:
    x = int(input('enter a number:'))
    y = int(input('enter a number:'))
    print(x / y)
except ZeroDivisionError:
    print('分母为0')
