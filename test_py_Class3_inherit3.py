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
print(c1[0] + c1[1])
print('访问序列次数', c1.counter)


# property()智能给成员变量分配值以及读取的方法
# 先看原始方法
class Rectangel:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size  # 这样的赋值方式使得size成为了元组

    def get_size(self):
        return self.width, self.height  # python能有多个返回值，牛逼


r1 = Rectangel()
r1.width = 10
r1.height = 5
print(r1.get_size())
r1.set_size((100, 150))
print(r1.width, r1.height)


# 使用property后
class Rectange:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_size(self, size):
        self.width, self.height = size  # 这样的赋值方式使得size成为了元组

    def get_size(self):
        return self.width, self.height  # python能有多个返回值，牛逼

    size = property(get_size, set_size)  # 只需要将get_size和set_size作为参数关联到property里面，然后重新命名一下就能使用property智能判别I/O方式
    # 条件：新式类 在老式python编译器里面使用__metaclass__
    # 深层：property是一个类，实现了一些__get__,__set__,__delete__方法，定义了描述符协议，将这些协议关联到寄生类的相关方法上


r = Rectange()
print(r.size)
r.size = 150, 100
print(r.width, r.height)


# property深层解析
class Rectangel2:
    def __init__(self):
        self.width = 0
        self.height = 0

    def __setattr__(self, key, value):  # __setattr__试图给属性赋值时自动调用
        if key == 'size':
            self.width, self.height = value
        else:
            self.__dict__[key] = value#__dict__是一个字典

    def __getattr__(self, item):  # 在属性被访问时而对象没有这样的属性时自动调用
        if item == 'size':
            return self.width, self.height
        else:
            raise AttributeError()
#效果和实现property的方法一致
r2=Rectangel2()
print(r2.size)
r2.size = 1500, 1000
print(r2.width, r2.height)