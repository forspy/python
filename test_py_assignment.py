# 导入模块(对象)
# import somemodule
# form somemodule import somefunction
# from somemodule import * 导入模块中的一切

# 相同方法的不同模块，需要这样调用
# moudle1.func()
# moudle2.func()

# 给模块指定别名调用as
import math as foobar

print(foobar.sqrt(4))

#赋值
x,y,z=1,2,3
print(x,y,z)
#快速交换变量
x,y=y,x
print(x,y,x)

#返回键
d={'bob':123,'lucy':456}
key=d.pop('bob')
print(key)
#返回键值
d1={'bob':123,'lucy':456,'lily':789}
key,value=d.popitem()
print(key,value)

#使用*来收集多余的赋值
a,b,*rest=[1,2,3,4]
print(a,b,rest)

a,*rest,b=[1,2,3,4,5]
print(a,rest,b)

#链式赋值
x=y=1
print(x,y)
#增强赋值
x+=1
print(x)