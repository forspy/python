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
