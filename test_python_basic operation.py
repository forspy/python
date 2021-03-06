print("hello world")
print(1 / 2)  # python的除法考虑小数
print(1 // 2)  # 这样是向下取整的除法
print(10 % 3)  # python求mod
# 多个字符串的连接输出
print("hello" + "world!" + '\n' + '!')  # 1.python的字符串连接方式 2.python识别\n
print("hello\nworld!")
print("c:\\test.txt")
print(r"c:\test.txt")
# reformat Code是自动对齐 快捷键：Ctrl+Alt+L
# 右键.py窗口，选择Show in explorer，可打开文件所在位置
# Ctrl+z 撤销
# Ctr+/ 注释和取消注释
# Ctrl+F5不调试运行
print(2 ** 3)  # 乘方
print(pow(2, 3))  # 乘方
print(abs(-11))  # 绝对值
print(round(5.1))  # 四舍五入
print(round(5.5))
print("------------------")
round(1.1)
print(0xAF)  # 十六进制 print的时候默认以十进制输出
print(0o10)  # 八进制
print(0b0011)  # 二进制
x = 10  # 变量

# print(y) #python变量没有初始化默认值，所以必须给每个python变量赋初值
# 在解释器中<<<2*2会输出4，但是在.py脚本中2*2不会有任何作用
# 获取用户输入
# y = input("y:")  # input里面是本文输出，可以通过赋值获取用户输入
# z = input("z:")
# print("y*z=", int(y) * int(z))  # 需要强转，或者说声明为int类型
# if流程判断
if x == 10:
    print("OK!")
# 导入模块并使用方法
import math  # 类似于导入头文件和建立对象(封装好的对象)

a = math.floor(3.2)  # 向下取整# 类似于使用对象方法
print(a)
b = math.ceil(3.2)  # 向上取整
print(b)
from math import sqrt  # 如果不考虑多个对象方法重名可以直接指定方法，省略对象名

c = sqrt(9)  # 返回double
print(c)

import cmath  # 复数对象

d = cmath.sqrt(-1)
print(d)
print((1 + 1j) * (1 - 1j))  # 复数运算

# -------------------------
# *是通配，就是导入turtle的全部的模块。用import turtle，下面的函数和数据前面都要加turtle.XXXXXX，
# 而用from turtle import * 就可以直接XXXXXX，而不需要turtle.了
# import Module #引入模块
# from Module import Other#引入模块中的类、函数或者变量
# from Module import * #引入模块中的所有公开成员
# ---------------------
from turtle import *

forward(100)  # 红线是pycharm的一个小bug
left(120)  # 转120度
forward(100)
left(120)
forward(100)
mainloop()  # 这句话可以保持窗口
# 方法一：
# from turtle import *
# #
# setup(300, 300, 100, 100)  # 设置界面为300*300
# pensize(2)
# pencolor('blue')
# circle(30)
# mainloop()
# 方法二：
# import turtle
#
# t = turtle.Turtle()
# turtle.setup(300, 300, 300, 100)
# t.pensize(2)
# t.pencolor('blue')
# t.circle(30)
# turtle.mainloop()
# 其中，turtle.Turtle()是一个画笔的对象。
# 有关绘制和设置画笔相关的就是画笔的属性。
# turtle.setup和turtle.mainloop设置的是画布的属性。

# 方法2、如开发过程中无需R，直接卸载R语言插件
# Files->Settings->Plugins->R Language Support->Uninstall
s = str(111)#将int转化成字符串
print(s)

#!/usr/bin/env python3
'''
大部分python文件的头部都会写上 #!/usr/bin/python 或者 #!/usr/bin/env ，这个语句主要和运行模式有关，
如果我们用普通运行模式例如(linux) ： python *.py 那么这个语句在此运行模式下无效。如果想让python程序像普通程序一样运行，
例如：./*.py (文件要有可执行权限chmod a+x *.py，然后执行./*.py)，这个语句就起作用了，他用来为脚本语言指定解释器，
通常认为用 #!/usr/bin/env python 要比 #!/usr/bin/python 更好，因为 python 解释器有时并不安装在默认路径，例如在虚拟环境中。
第一：#!/usr/bin/env python
这种写法在你机器上安装了多个版本的python的时候有意义，这样声明的时候，会去取你机器的 PATH 中指定的第一个 python 来执行你的脚本。
如果这时候你又配置了虚拟环境的话，那么这样写可以保证脚本会使用你虚拟环境中的 python 来执行。
第二：#!/usr/bin/python
表示写死了就是要 /usr/bin/python 这个目录下 python 来执行你的脚本。这样写程序的可移植性就差了，如果此路径下python命令不存在就会报错。
所以一般情况还是用第一种写法。
'''
