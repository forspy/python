# 下面使用list对象的方法，即成员函数
lst = [1, 2, 3]
lst.append(4)  # 尾部追加
print(lst)
lst.clear()  # 清空链表
print(lst)

# 常规赋值 其实是变量的引用
a = [1, 2, 3]
b = a
a[1] = 22
print(b)  # [1, 22, 3]
b = a.copy()
a[1] = 22222222
print(b)  # [1, 22, 3]  .copy()会重新创建一块内存存放b对象

# count方法 统计指定的元素出现了几次
x = [1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 3]
print(x.count(3))

# extend 方法附加多个元素到链表末尾
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
# 用切片的方式也行
c = [1, 2, 3]
d = [4, 5, 6]
c[len(c):] = d
print(c)

# index 方法 查找值第一次出现的索引
str = ["hell", 'oooo', 'we']
print(str.index('we'))  # 如果没找到则会返回异常
# pycharm帮助文档
# 把光标放在要查询的对象上，打开视图菜单，quick definition查看对象的定义，quick documentation 快速文档，这个是jet brains自己对python的解释文档，
# 第三个external documentation 外部文档，这个是python 的官方帮助文档，调转到网页帮助文档中。

# insert 方法
numbers = [1, 2, 3, 5, 6]
numbers.insert(3, 'four')
print(numbers)
# 对比切片插入法
numbers[1:1] = ['two']
print(numbers)
# 个人还是比较喜欢调用对象方法

# pop 方法 弹出一个元素
a = [1, 2, 3]
a.pop()  # 默认弹出尾部
print(a)
pop_value = a.pop(0)  # 使用pop()返回一个弹出的值
print(a)
print(pop_value)
# 比较del 切片删除a[1:1]=[]
# 个人还是比较喜欢对象方法
# python的push使用的是append()方式 push和pop形成了栈的压入和弹出

#remove 方法 删除第一个为指定值的元素，相当于count和pop的结合
x=['we','are','family']
x.remove('are')
print(x)

#reverse 方法 逆转链表
x=[1,2,3]
x.reverse()
print(x)

#sort 方法 对链表进行排序,默认升序
x=[1,43,345,123,546,34,2,234,2]
x.sort()
#注意.sort()不返回值 不能就地赋值y=x.sort() 可以分开赋值 或者使用y=x.copy() 或者使用y=x.sorted()
print(x)
#逆序可以使用参数reverse
m=[23,12,43,324,3]
m.sort(reverse=True)
print(m)
#sort的另一个参数key 指定按照什么标准进行排序
n=['we','are','family','!']
n.sort(key=len)#表示按照字符串长度进行排序
print(n)