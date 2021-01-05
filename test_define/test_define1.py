#高效复用
def function1(str1,str2):
    print(str1,str2)
    str=str1+str2
    return str
a='hello'
b='world'
#注意，程序是自上而下运行的，所以先要运行上面的代码段
name=function1(a,b)
print(name)

#关于def中的数据传递与变量储存

def fun01(a,b,c):
    a=100#局部变量
    b[0]=200#深拷贝
    c=300#局部变量

n1=1
n2=[2]#列表是创建在全局的
n3=[3]
fun01(n1,n2,n3)
print(n1)#1
print(n2) [200]
print(n3) [3]

#不可变的数值型（整数、浮点数、复数）
#布尔值bool
#None空值
#字符串
#元组tuple
#固定集合
#开辟在const value上


#可变的类型参数
#列表
#字典
#集合set
#字节数组bytearray
#开辟在堆栈上