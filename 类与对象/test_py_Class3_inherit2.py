# 继续来讲继承
# 继承多个基类,即多重继承
class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)  # 计算这个expression表达式，并存入value里面


class Talker:
    def talk(self):
        print('hi,my value is', self.value)


class TogetherCal(Calculator, Talker):
    pass


tc = TogetherCal()
tc.calculate("1+2*3")
tc.talk()
# 1.这里面因为TogetherCal继承了Calculator和Talker，所以当使用tc.calculate("1+2*3")的时候self.value成员变量被创建并赋值
# 2.然后再调用tc.talk() ，因为self.value里面有值，所以能够输出
# 3.这里注意不能使用一般变量value来记录eval()的输出，因为是一个局部变量不能共享，self.value则类似于全局变量 可以实现共享
# 另外类的次序要注意，如果基类里面实现的多个同名的方法，在继承时后面的基类方法会覆盖掉前面的方法 ，具体见方法解析顺序(MRO)

# 判断一个类中有没有某个成员函数
print(hasattr(tc, 'calculate'))

# setattr可用于设置对象的属性
setattr(tc, 'name', 'bob')  # 有成员变量的修改，没有成员变量的创建成员变量
print(tc.name)
# .__dict__查看tc对象的成员变量和值
print(tc.__dict__)  # 查看tc对象的成员变量和值

#具体研究类的组成可以使用inspect模块
import inspect

#抽象基类
#结构
from  abc import ABC,abstractclassmethod#引入抽象基类模块

class Talker(ABC):
    @abstractclassmethod#使用@abstractclassmethod将方法标记我抽象
    def talk(self):
        pass

#T=Talker()#Can't instantiate abstract class Talker with abstract methods talk 抽象基类不能实例化

#派生出来的类也需要重写
class Knigget(Talker):
    def talk(self):
        print('继承抽象类')

T_inherit=Knigget()
T_inherit.talk()
