# t1=[1,1,1]
# t2=[2,2,2]
# t3=pow(t1,2)+pow(t2,2)
# print(t3)
#这样是会报错的，因为pow()不支持t1位list输入

#引入数组代替标量进行运算
#将原本只能处理标量的函数变得可以处理矢量
import numpy as np
import math
def foo(x,y):
    return math.sqrt(x**2+y**2)#注意**2才是乘方，^2不是

x=3
y=4

print(foo(x,y))
X=np.array([3,4,5])
Y=np.array([4,5,6])
v_foo=np.vectorize(foo)#对函数指针进行操作
print(v_foo(X,Y))

#同理
t1=[1,2,3]
t2=[2,2,3]

def fun(x,y):
    return x**y
v_fun=np.vectorize(fun)#
print(v_fun(t1,t2))


print(np.power(t1,t2))#使用np的内置方法可以直接矢量化