# 迭代器协议
# 前面使用for循环进行过序列和字典的，但实际上也可以迭代其他对象，实现了方法__iter__的对象

# 方法__iter__返回一个迭代器，这个迭代器是一个对象并且里面有一个__next__的方法

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):  # 实现next方法才可返回下一个
        self.a, self.b = self.b, self.a + self.b  # 注意这两个等式是同时进行的
        return self.a  # 返回数列中的下一个

    def __iter__(self):  # 实现__iter__方法表示Fibs()类是可迭代的
        return self


fibs = Fibs()

for f in fibs:
    if f > 10:
        print(f)
        break

# 下面来对比一下其他Fibs的实现方法
# 直接使用list链表容器
fibs1 = [0, 1]
for i in range(0, 8):  # 表示进行8次循环
    fibs1.append(fibs1[-2] + fibs1[-1])  # 每次在尾部增加一个数，该数是链表中的前两个数的和
print(fibs1)


# 通过函数定义
def fibs_func(num):
    '设置一个斐波那契数列'  # python特有的函数文档，写入函数体中用于说明
    result = [0, 1]
    for j in range(0, num - 2):
        result.append(result[-2] + result[-1])
    return result


fibs2 = fibs_func(10)
print(fibs2)

# 我们可以看到，以上两种方式都使用了list容器，其实list容器里面已经实现了iterator，相当于大炮打蚊子
# 其他迭代器的方法
it = iter([1, 2, 3])  # 这样it就是一个迭代器对象， 对象=iter(对象)
print(next(it))
print(next(it))


# 还可以使用迭代器生成有限序列其实就是for循环的机制
class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value

    def __iter__(self):
        return self


it = TestIterator()
print(it)
print(list(it))  # 使用list将迭代器显式转换为列表

print(list('hello'))  # 机制是一样的，list的显示机制是一样的
