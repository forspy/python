# 简单推导
print([1, 2, 3])
print([x * x for x in range(0, 10)])  # 使用for循环进行简单推导形成列表
print([x * x for x in range(0, 10) if x % 3 == 0])  # 还可以通过在for循环中加入条件进行推导
# 可以实现元组链表的推导
print([(x, y) for x in range(0, 3) for y in range(0, 3)])
# 与下面的作用一致
result = []
for x in range(0, 3):
    for y in range(0, 3):
        result.append((x, y))
print(result)

# 简单推导还可以用于快速配对
girls = ['alice', 'lily', 'bob']
boys = ['lucy', 'slina', 'alex']
test = [b + g for b in boys for g in girls if b[0] == g[0]]
print(test)
# #算法优化
# girls = ['alice', 'lily', 'bob']
# letterGirls={}
# for girl in girls:
#     letterGirls.setdefault(girl[0],[]).append(girl)
# print(letterGirls)
# print([b+g for b in boys for g in letterGirls[b[0]]])

# 字典推导
squares = {i: "{} squares is {}".format(i, i ** 2) for i in range(0, 4)}
print(squares)  # {0: '0 squares is 0', 1: '1 squares is 1', 2: '2 squares is 4', 3: '3 squares is 9'} 将i和字符串形成pair组成字典
print(squares[2])

# pass 空代码块 即什么都不做 python的机制时一定要有执行代码，所以pass的出现解决了这个问题
name = input("请输入你的名字:")
if (name == 'bob'):
    print('hello' + name)
elif (name == 'lucy'):
    print('hello' + name)
elif (name == 'lily'):
    pass

# python的自动释放内存机制
x1 = {'bob': 123, 'lily': 456}
x2 = x1
del x1  # 删除这个名称
# x1 = None 与del的效果有区别 del是包括变量名都删除，即访问不到这个变量了
print(x2)
x2 = None
print(x2)
# 在不使用这个变量后python的智能指针会去释放这一块变量对应的内存

#炒鸡强大的功能来了，exce()执行字符串的计算结果，智能分析使用其中的函数，类似于函数指针
exec("print('hello world')")#输出hello world
#exec()就像黑魔法一样，带给你强大功能的同时也会有负面效果，比如污染你的函数命名空间
#因此我们在使用的使用通常创建一个字典来表示命名空间
from math import sqrt
scope={}
exec('sqrt=81',scope)#使用exec实现了sqrt=81的赋值语句
print(scope['sqrt'])

#eval实现计算器
print(eval(input('请输入：')))
