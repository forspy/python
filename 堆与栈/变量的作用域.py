#创建一个全局变量，在堆上开辟内存
#全局变量可以定义在一个程序里面，也可以定义在多个py文件里面，通过模块调用的方式获取
g01=1

def fun01():
    print(g01)
    l01=2#局部变量只能在函数段内使用，在栈上开辟内存

fun01()

g02=1

def fun02():
    global  g02#修改全局变量 相当于C中的指针*(&parameter)
    g02=2
    global  g03#可以在局部代码段创建全局变量
    g03=3
    return g02

fun02()
print(g02)
print(g03)