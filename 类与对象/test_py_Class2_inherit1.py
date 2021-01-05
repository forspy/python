# 这里来讲一下python的关联机制
class Test:
    def method(self):
        print('class Test method')


def func():
    print('fun() out')


instance = Test()
instance.method()
instance.method = func  # 改变指向,类的方法函数指针实际上已经替换为func哈数指针

instance.method()


# 直接指向类内的方法
class Bird:
    song = 'HAAAA!'
    __privatSong = 'HBBBB!'  # 这样在外部就拿不到privatSong这个变量了因为使用__标记了私有属性

    def sing(self):
        print(self.song)

    def sing1(self):
        print(self.__privatSong)  # 可以在内部访问__privatSong私有变量


bird = Bird()  # 实例化一个类
bird.sing()

birdsing = bird.sing  # 创建一个函数指针birdsing
birdsing()

print(bird.song)  # 可以直接访问song的成员变量

bird.sing1()  # 外部进行


# 类继承
class Filter:
    def init(self):
        self.blocked = []

    def filter(self, sequence):  # 过滤器
        return [x for x in sequence if x not in self.blocked]  # x在sequence里面遍历 并且x不在blocked链表里面


class selectFilter(Filter):  # 继承Filter
    def init(self):  # 重写基类的方法
        self.blocked = ['SPAM', 'SAM']


f = Filter()  # 实例化一个类对象
f.init()  # 注意init()并非一个构造函数，而是一个普通方法 如果想要取得blocked的值，则需要先进行init()的初始化
print(f.blocked)
print(f.filter([1, 2, 3]))  # 因为基类的blocked链表为空，所以不会过滤

# 通过派生类过滤
s = selectFilter()
s.init()
print(s.filter(['SPAM', 'SAM', 'HTTP', 'SIMP', 'SSL']))  # 完成过滤

# 判断一个类是否是基类的派生
print(issubclass(selectFilter, Filter))
# 查询一个类的基类
print(selectFilter.__bases__)  # (<class '__main__.Filter'>,)

# 确定对象是否是特定类的实例
print(s)  # <__main__.selectFilter object at 0x0000027951E3D668>


