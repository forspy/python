# 字典方法clear 清空字典
d = {'bob': 123, 'lucy': 456}
d.clear()
print(d)
# 字典浅拷贝--并未开辟空间，只是生成了指向原空间的指针，半独立
d = {'bob': 123, 'lucy': 456}
d_copy = d.copy()
d_copy['bob'] = 111
print(d)
print(d_copy)

# 深拷贝--这样就完全独立了
from copy import deepcopy

d_deepcopy = deepcopy(d)
print(d_deepcopy)

# 使用get访问不存在的键时不会发生异常
print(d.get('bbb'))  # 没有找到返回None

print(d.get('bbb', '没有找到'))  # 也可以返回自定义值

# items返回(key,value)的键值对
print(d.items())

# pop弹出一对键值，并返回值
print(d.pop('bob'))

# popitem 方法，随机弹出一对键值

# 添加键值方法
d['lily'] = 789
print(d)

# setdefault 有键返回值，无键创建键值
d.setdefault('bob', 'new')

print(d)

# d.update(x)使用x来更新d
x={'bob':999}
d.update(x)
print(d)

#values 返回字典中的值视图 非链表
d_val=d.values()
print(d_val)