# 字符串继承序列的操作：索引、切片、乘法、长度、最大、最小值...
# 字符串不可变，序列的元素赋值和切片赋值时非法的
a = 'abc'
# a[0] = 'A'  # TypeError: 'str' object does not support item assignment

# 字符串转换说明符
str = "hello,%s"
str1 = "world"

print(str % str1)

text = "123%d"
value1 = 4
print(text % value1)

# 其他解决方案:字段替换
from math import pi

print("{name} is {value:.2f}".format(value=pi, name="pi"))
from math import e

print(f"e is {e}")  # 使用f简写形式

num = 12345
print(f"value is {num}")  # 使用f简写形式

#二进制转换
v=20
print(f"20 的二进制 {v:b}")

print('{1} {1} {0}'.format('hello','world'))

#for i in range(0,3):
#    name=input("请输入第%d个学生的姓名："%(i+1))
i=0
string_list=[]
#int 为%d float为%f str为%s
while True:
    name=input("请输入第%d个学生的姓名"%(i+1))
    i+=1
    if name=='esc':
        break
    string_list.append(name)

print(string_list)