class CounterList(list):  # 继承list的方法
    def __init__(self, *args):
        super().__init__(*args)  # 调用list基类的构造函数
        # 也可以使用super(CounterList, self).__init__(*args) 调用基类方法
        self.counter = 0

    def __getitem__(self, item):
        self.counter += 1  # 计数器累加
        return super(CounterList, self).__getitem__(item)  # 表示调用基类的__getitem__()方法


c1 = CounterList([1, 2, 3, 4, 5])
print(c1)
c1.reverse()
del c1[0]
print(c1)
print(c1[0]+c1[1])
print('访问序列次数',c1.counter)