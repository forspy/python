# 1.模块time
import time

print(time.asctime())  # Thu Mar 14 09:30:20 2019  显示当前时间
# 模块time中的一些重要函数
# time.sleep(1)  # 进程阻塞 让进程休眠几秒

# 2.模块random
import random

print(random.random())  # 返回0-1的一个随机数
print(random.uniform(1, 10))  # 返回一个1-10的随机实数
print(1.11 // 1, 1.54 // 1)  # 可以以这种方式返回整数,取floor
print(random.randrange(1, 11))  # 随机生成整数
print(random.randrange(1, 11, 2))  # 随机生成奇数
l = [1, 2, 3, 4, 5]
print(random.choice(l))  # 从序列中随机抽取一个数
print(random.sample(l, 2))  # 随机抽取指定数量的元素
random.shuffle(l)  # 随机打乱序列
print(l)
from time import *  # 这样写可以直接写函数，但我个人不喜欢

date1 = (2018, 1, 1, 0, 0, 0, -1, -1, -1)  # 年月日时分秒 星期-1 儒略日-1 夏令时-1
time1 = mktime(date1)
print(time1)
data2 = (2019, 1, 1, 0, 0, 0, -1, -1, -1)
time2 = mktime(data2)
# 随机生成这个时间段内的时间
random_time = random.uniform(time1, time2)
print(asctime((localtime(random_time))))

values = list(range(1, 11)) + 'Jack Queen King'.split()
print(values)
suits = 'diamonds clubs hearts spades'.split()
deck = ['{} of {}'.format(v, s) for v in values for s in suits]  # 一共52种
print(len(deck))
random.shuffle(deck)  # 打乱这副牌
print(deck[0:14])

# 3.模块shelve 文件储存
import shelve
import sys

s = shelve.open('1.dat')
s['x'] = ['a', 'b', 'c']
print(s['x'])
s.close()


# 来看一个数据库的例子 跟字典很像，但是这里使用shelve创建了文件 用于创建永久性映射
def store(db):
    pid = input('请输入编号:')
    person = {}
    person['name'] = input('请输入姓名：')
    person['age'] = input('请输入年龄：')
    db[pid] = person  # 两层字典


def lookup(db):
    pid = input('请输入编号:')
    print(db[pid]['name'], db[pid]['age'])


def main():
    database = shelve.open('person.dat')
    try:
        while True:
            cmd = input('请输入指令 store存，lookup取 quit退出:')
            if cmd == 'store':
                store(database)
            if cmd == 'lookup':
                lookup(database)
            if cmd == 'quit':
                return
    finally:
        database.close()


if __name__ == '__main__': main()#表示适用于本程序，但也可被其他程序调用

#如果要以这样的格式保存数据，也就是让其他语言编写的程序能够轻松地读取它们，可考虑使用JSON格式。python提供了处理JSON字符串的JSON模块
# JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。
# 在 JS 语言中，一切都是对象。因此，任何支持的类型都可以通过 JSON 来表示，例如字符串、数字、对象、数组等。但是对象和数组是比较特殊且常用的两种类型：
# 对象表示为键值对
# 数据由逗号分隔
# 花括号保存对象
# 方括号保存数组
#另外也可以了解一下xml数据传输文档