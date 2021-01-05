#关于局部代码段上的栈变量与堆变量上的区别

def fun01(a,b,c):
    a=100#修改栈上的变量
    b[0]=200#修改堆上的变量
    c=300#修改栈上的变量

num1=1
num2=[2]
num3=[3]

fun01(num1,num2,num3)

print(num1,num2,num3)