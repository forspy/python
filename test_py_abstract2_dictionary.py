# 先来看一个多重结构的字典
# 为了储存一个人员的特征需要使用多个参数来表示
people = {}


def init(people):
    people['weight'] = {}  # 二级字典
    people['height'] = {}
    people['sex'] = {}


init(people)
print(people)
# 形成对应
people['weight']['overload'] = ['bob', 'Tim']  # 表示weight类字典里的overload属性
people['weight']['light'] = ['lily', 'lucy']
people['weight']['middle'] = []
people['sex']['female'] = ['lucy', 'lily']
people['sex']['male'] = ['bob', 'Tim']
people['height']['tall'] = ['bob']
print(people)
print(people['height']['tall'])


def lookup(object, lab, parameter):
    return object[lab][parameter]  # 返回一个list，这里面的字典key值必须先初始化好


def store(object, lab, parameter, list):
    list1 = lookup(object, lab, parameter)
    if (not list1) or (list1 != list):  # 如果list1为[]或者list1与list不相同就修改
        people[lab][parameter] = list  # 这里面的people使用全局对象people
    return


print(people['weight']['middle'])
store(people, 'weight', 'middle', ['lucy'])
print(lookup(people, 'height', 'tall'))
print(lookup(people, 'weight', 'middle'))


# 默认参数设置
def func(name='bob', action='fight!'):
    print('{} is {}'.format(name, action))
    return


func('lily', 'beaten')
func()


# 大量参数的输入使用*参数来把这些未知个数的参数形成元组后输入
def print_parmas(title, *params):
    print(title)
    print(params)  # 参数为元组的地址


a = 1
print_parmas('test', a, 2, 3, 4, 5)


# c/c++需要传入地址print_parmas('test',&a) 然后用指针接住这个地址，但python省略了中间的类型一致的判定

# 如果多个参数在中间，在调用的时候需要在后面指定
def func1(a, *b, c):
    print_parmas(a, b)
    print(c)


func1('test', 1, 2, 3, 4, c=5)


# 注意分析中间的结果
# test
# ((1, 2, 3, 4),)
# 5

# 要收集关键字参数可以使用**，输出为字典
def func2(**params):
    print(params)


func2(x=1, y=2, z=3)  # 这样输出就会形成字典


# 通过*分配元组参数
def add(x, y):
    return x + y


params = (1, 2)
print(add(*params))  # 通过*分配参数


# 字典参数传入
def story(**kwds):  # 收集参数，得到的kwsds是一个字典对象
    print('{job} is a {name}'.format_map(kwds))  # format_map的参数是字典对象


# 方法1.传入字典
tt = {'job': 'python', 'name': 'lanuage'}
story(**tt)  # 将字典分配为参数传入
# 方法二.传入参数
story(job='c++', name='lanuage')
# 方法三 混合传入
tt2 = {'name': 'lanuage'}
story(job='java', **tt2)


# 元组参数传入

def power(x, y, *others):
    if (others):
        print('接收到其他参数', others)
    return pow(x, y)


print(power(2, 3))
params = (5,) * 2  # (5, 5)
print(power(*params))  # 将元组分配为参数传入
print(power(*params, '随便输入'))


# 测试默认参数
def interval(start, end=None, step=1):
    if end is None:
        start, end = 0, 0
    result = []

    temp = start
    while temp < end:
        result.append(temp)
        temp += step
    return result


print(interval(0, 10))
print(interval(0, 10, 2))
