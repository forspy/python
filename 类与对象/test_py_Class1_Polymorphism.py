# 对象的三大特性：封装、继承、多态
# 封装：使用private protect public来控制成员变量/成员函数的访问权限 使得类对象的private数据结构部分隐藏，用户智能调用public部分的方法，从而起到封装的效果
# 继承可以使用通用类创建出专用类来实现代码的高效复用
# 多态基于继承上面发展的基类对象指针调用派生类方法(函数的重载在python里也算为多态)

# 多态
# c++的多态主要通过virtual虚函数来实现 目的是在基类对象和派生类对象同时写有同名的方法时，
# 增加virtual说明后，派生类对象（Derived class object）能够使用派生类对象的方法
# // 上面的测试表明，原来是什么类型就能调用该类型的方法
# C
# obj_c;
# D
# obj_d;
# obj_c.func();
# obj_d.func();
# C * c1 = & obj_d; // C
# 类型的c1对象指向了D类
# C & c2 = obj_d;
# c1->func(); // 输出
# 'D'
# 这里出现了多态
# c2.func(); // 输出
# 'D', 引用也同理产生了多态
# python的多态主要指的是对于不同的对象能够使用相同的方法名产生不同的效果

# 使用random随机从序列里面选出一个值
from random import choice

x = choice(['hello', 'world', 1, 2, 3, 4, 5])
print(x)
# 函数的重载在python里也算为多态

# 来看看多态的集大成者repr()
print('abc')
print(repr('abc'))
print([1, 2, 3])  # print()的多态实现得也很全面
print(repr([1, 2, 3]))

# 这里python说了这样一句话 要破环多态，唯一的办法是执行类型检查 比如type issubclass
# 但是重要的是对象按照你希望的那样行事，而不用考虑它是否是正确的类型(这又回到了c++里面严格的多态本质)
# 鸭子类型通俗易懂的解释了多态：如果走起来像鸭子，叫起来像鸭子，那么它就是鸭子

# c++的基类和派生类在python中被称为超类和子类

__metaclass__ = type  # python2 需要这个代码


class Person:
    # 定义类方法
    def setName(self, name):
        self.name = name;  # self.name 相当于成员变量 self相当于*this，指向这个对象本身

    def getName(self):
        return self.name;
    def greet(self):
        print("hello,world!I'm {}".format(self.name))
#实例化对象
foo=Person()
bar=Person()

foo.setName('bob')
bar.setName('lily')

foo.greet()
bar.greet()

#创建一个类
class Wife:
    #初始化类中的成员变量
    def __init__(self,name,age):#构造函数，self指的是对象指针
        self.name=name
        self.age=age
    def Message(self):
        print(self.name,' ',self.age)
    def cooking(self):
        print(self.name+'做饭')
#实例化对象
dearHu=Wife('zhizhibao',30)#示例化的过程中会调用类中的构造函数__init__

dearHu.Message()

dearHu.cooking()

#在类中，方法只有一个，而类对象可以创建多个

#通过类名使用类方法
class Husband:
    #计数器
    #全局成员变量--示例方法和类方法均能使用
    count=0
    __number=0#私有成员private 对象访问不到，只能通过方法访问，这样就有了封装的效果
    def __init__(self):
        Husband.count+=1 #注意一定是全局成员 Husband.count+1 而不是self实例化对象的成员+1

        #实例成员变量
        self.name=''
    def getNumber(self):
        return self.__number
    @classmethod#注意@classmethod的标注只对下一个def有效
    #标记为一个类方法
    def getCount(cls):
        #操作全局成员变量
        return cls.count
    #静态方法--不需要self/cls对象
    @staticmethod
    def staticGetCount():
        pass
h1=Husband()
print(h1.getCount())
h2=Husband()
print(h2.getCount())

print(Husband.getCount())#直接返回类的成员变量
print(h1.count,h2.count)
print(h1.getNumber())#通过这种方式拿到私有成员变量的值

