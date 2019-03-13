# python中的数据结构
# 1.集合set
print(set(range(10)))
print(set([1, 1, 1]))  # set只接受同一元素最多一个
print({1, 2, 3, 4, 5, 6, 6, 6})  # 花括号也能创建set
# 2.堆heap
# 这里的堆表示一种数据结构 它时一种优先队列 功能：能够以任意顺序添加对象 并找出最小元素 （相对于min方法效率高得多）
# python里面的堆数据结构需要依靠模块导入
from heapq import *
from random import shuffle

data = list(range(10))
shuffle(data)  # 随机排序列表
print(data)
heap = []  # 创建一个heap对象
for n in data:  # 遍历data,python的另一个特点是遍历机制简单 相较于c/c++的下标位置来说 python直接在for循环里面拿到了该值 但有利有弊
    heappush(heap, n)  # 将n压入堆

print(heap)  # 这里有一个问题就是顺序压入堆以后，堆又进行了调整,但是不管怎么调整，堆的第一个元素必定是最小值

print('3//2=', 3 // 2)
# 堆排序的特征 位置i处的元素总是大于位置i//2处的元素
for i in range(10):
    print(heappop(heap))  # heappop能弹出堆中最小的元素

l = [12, 234, 234, 34, 1, 34, 5, 6, 6]
heapify(l)  # heapify快速将一个列表转化为堆结构 ，那么转化为堆数据结构有什么好处呢？待解决
print(l)

# 3.双端队列deque
from collections import deque

q = deque(range(0, 4))
q.append(5)
q.appendleft(6)
print(q)
q.rotate(1)  # 依次往后移动一位
print(q)
q.rotate(-1)  # 依次往前移动一位
print(q)
# 双端队列是循环链表
