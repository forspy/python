# 元组Tuple也是序列，但是不能被修改
Tuple1 = (1, 2, 3)
print(Tuple1)
Tuple_Nan = ()
Tuple_one = (1,)
Tuple_cal = 3 * (40 + 1,)
print(Tuple_cal)

# 序列和元组的转化
T_tran1 = tuple([1, 2, 3])
T_tran2 = tuple('abc')
T_tran3 = tuple(T_tran1)
print(T_tran1, T_tran2, T_tran3)

# 元组的访问方式和序列一致
x = (1, 2, 3)
print(x[1])
print(x[0:1])

# 元组的特点是:1.作用映射中的键，而列表不行2.有些内置函数和方法返回元组
