# while循环
x = 1
while (x <= 5):
    print(x)
    x += 1  # python的缩进控制了作用域的范围

# for循环
# 遍历
words = ['this', 'is', 'a', 'word']
for word in words:
    print(word)

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)
# python 为遍历创建了一个内核函数range
a = list(range(0, 5))
print(a)
print(range(0, 5))

# 将range()用于遍历
for num in range(0, 3):
    print(num)

# for 遍历字典
d = {'bob': 123, 'lucy': 456}
for key in d:
    print(key, ':', d[key])
