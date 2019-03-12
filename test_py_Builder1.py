# python的两大新特新 迭代器个生成器
# python生成器
nested = [[1, 2], [3, 4], [6, 5, 7]]  # 这是一个由列表组成的列表，那么想要将其中的每个元素提取出来重新组成一个列表


def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element  # yield就是一个生成器


# 生成器的特点 不同于return返回一个值，而是可以生成多个值，每次一个，每次yield生成一个值以后，函数将冻结，等待被重新唤醒从停止的地方继续

for num in flatten(nested):
    print(num)

print(list(flatten(nested)))

# 比较一下生成器推导和列表推导
# a.列表推导
print([x * x for x in range(0, 10)])  # 使用for循环进行简单推导形成列表
print([x * x for x in range(0, 10) if x % 3 == 0])  # 还可以通过在for循环中加入条件进行推导

# b.生成器推导
g = (x * x for x in range(0, 10))  # 注意生成器推导使用圆括号
for i in range(0, 10):
    print(next(g))  # 每一次出现一个，有点debug的意思


# 递归式生成器：对于任意层嵌套的列表使用
def Recursive_flatten(nested):
    try:
        # 加入判别字符串的机制
        try:
            nested + ' '  # 列表不可以加单个元素，列表只能合并，只有在分解为'ass'这样的单个字符串元素后才能合并' '
        except TypeError:
            pass
        else:
            raise TypeError  # 这种情况下才表示单个字符串元素
        for sublist in nested:
            for element in Recursive_flatten(sublist):
                yield element
    except TypeError:  # 如果只有一个数，就直接生成这个数，但是如果是字符串就存在问题，因为字符串是序列，并不存在最小单元
        yield nested


str_test = ['a', 'b', ['c', 'd'], 1, 2, 3]
print(list(Recursive_flatten(str_test)))  # 这样，不管列表有几层嵌套，都可以使用递归式生成器生成
# a=[1,2,3,[1,2]]
# b=a+' '#TypeError: can only concatenate list (not "str") to list
a = [1, 2, 3]
b = a + [1]  # 列表和列表之间可以合并


# 进一步剖析生成器，生成器由生成器的函数和生成器的迭代器（指针）组成 生成器的迭代器是这个函数返回的结果 一般返回一个地址
# 通过list传入这个指针（迭代器）便能重构一项项的元素，形成链表
def repeater(value):
    while True:
        new = (yield value)  # 如果调用的是send那么yield返回一个send的参数 如果调用的是next那么yield返回None
        if new is not None: value = new
        # value+=1


r = repeater(42)
print(next(r))
print(r.send('hello'))  # send的使用一般需要在next的后面
print(next(r))


# 老版本的python没有生成器 那么使用以下方法来模拟生成器
def flatten_old(nested):
    result = []
    try:
        try:
            nested + ' '
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten_old(sublist):
                result.append(element)
    except TypeError:
        result.append(nested)
    return result


# 生成器的特点是中断并输出 但其实质是分解链表元素并添加到链表的尾部 在使用生成器的时候你可以使用next一次次输出，也可以send参数，也可以使用list一次性输出

print(flatten_old([1, 2, ['hello', 4]]))  # 老式的生成器是一次性输出的，原理是递归分解
