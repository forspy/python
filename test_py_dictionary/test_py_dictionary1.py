# 键-值：通过键(word)，找值(value)
# 键值的map组合怎么实现呢，先看一种原始的做法
names = ['bob', 'lucy', 'lily']
numbers = [123, 456, 789]
# 需求：找lucy的值
print(numbers[names.index('lucy')])

# 创建字典可以更方便地解决问题，键必须不同，值可以相同
phonebook = {'bob': 123, 'lucy': 456, 'lily': 789}
print(phonebook)
# 也可以使用dict()通过键值对创建
# 键值对 每一对是一个元组
items = [('bob', 123), ('lily', 456), ('lucy', 789)]
d = dict(items)
print(d)
# 使用字典
print(d['lucy'])

# 字典地基本操作
# len 返回几对
print(len(d))
# d[键]返回值
print(d['bob'])
# d[键]=新值，将新值关联到该键
d['bob'] = 111
print(d['bob'])

# del删掉一对键值
del d['lily']
print(d)

# k in d检查字典d中是否有k键
print('bob' in d)

# 键地类型可以是int string 和元组

# 字典较列表的优势
# x=[]
# x[42]='bob'
# IndexError: list assignment index out of range 需要[None]*43先开辟空间
x = {}  # 创建一个空字典
x[42] = 'bob'  # 这将创建一个字典{42: 'bob'}
print(x)

# 实例：一个简单的数据库
people = {
    'bob': {
        'phone': '123',
        'address': 'xxx1xxx'
    },
    'lucy': {
        'phone': '456',
        'address': 'yyyy1yyyy',
    }
}

labels = {'p': 'phone number', 'a': 'address'}
name = input('请输入要查询的名字:')
request = input('phone number(p)or address(a):')

if request == 'p': key = 'phone'
if request == 'a': key = 'address'

if name in people: print('{}的{}是{}'.format(name, labels[request], people[name][key]))

#字典配合format
d={'bob':123,'lucy':456}
print('bob phone number is {}'.format(d['bob']))
print('bob phone number is {bob}'.format_map(d))

#print(people.items())