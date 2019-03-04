# 构造函数，在实例化对象的时候能够自动调用，构建成员函数
class FooBar:
    def __init__(self):  # 构造函数,服，python的构造函数只能写成__init__
        self.var = 42


f = FooBar()
print(f.var)


# 给构造函数赋值参数
class FooBar1:
    def __init__(self, value=42):  # 构造函数里面可以加载参数
        self.somevar = value


f1 = FooBar1('parameter')
print(f1.somevar)


# 析构函数__del__同理可以使用，只不过python会使用智能指针自动释放成员变量内存

# python的重写机制
class A:
    def hello(self):
        print('A')


class B(A):
    pass


a = A()
b = B()

a.hello()  # A
b.hello()  # A,因为B类没有实现自己的方法所以从A类里面寻找方法 这个是python多态较好的体现


# 如果说C类实现并重写了A类的方法
class C(A):
    def hello(self):
        print('C')


c = C()
c.hello()  # C各自实现自己的方法
a.hello()  # A


# 派生类继承基类的构造函数
# c++里面的派生类基于基类构造函数
# BrassPlus::BrassPlus(const string & s, long an, double bal, double ml, double r):Brass(s,an,bal)
# //1.利用基类的构造函数进行代码复用。2.也需要为基类成员赋值，因为派生类继承了基类的所有成员，只是private不能访问，但还是要给他们赋值

# python在派生类需要新构建成员变量的时候是怎么解决问题的呢？
# 1.调用未关联的超类构造函数
# 2.使用函数super

# 先来看第一种
class Bird:
    def __init__(self):
        self.hungrey = True

    def eat(self):
        if self.hungrey:
            print('小鸟饿了，要吃饭饭！')
        else:
            print('小鸟饱饱，\(￣︶￣*\))，舒服~')


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)  # 调用基类的构造函数
        self.sound = '咕咕~'

    def sing(self):
        print(self.sound)


sb = SongBird()
sb.sing()  # 调用派生类方法
sb.eat()  # 调用基类方法


# 2.使用函数super
class SongBird1(Bird):
    def __init__(self):
        super().__init__()  # 调用基类的构造函数,使用super()即使有多个基类也只需要调用super()一次(基类的构造函数也得使用super())
        self.sound = '咕咕1~'

    def sing(self):
        print(self.sound)


sb1 = SongBird1()
sb1.sing()  # 调用派生类方法
sb1.eat()  # 调用基类方法
