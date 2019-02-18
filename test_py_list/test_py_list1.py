str = list('hello')
print(str)  # ['h', 'e', 'l', 'l', 'o'] 这样是链表
str1 = ['hello']
print(str1)  # ['hello'] 这样赋值是序列
# 列表的特点是可以对序列中的元素做修改
a = [1, 2, 3]
a[1] = 22
print(a)
# 对比
# a_list=list(1,2,3)  这条是错误的写法 list对象的构造参数最多1个
# py中的sequence和list都能写成一种形式[]
# 删除元素
del a[2]
print(a)
print('len:', len(a))

# 给切片赋值
# 字符串序列不支持切片改变元素
str1[2:] = ['aaa']
print(str1)
#对比序列切片 可以支持长度不同的替换
str[2:] = list('aaaaaaa')
print(str)
#list的插入
str[1:1]=[1,2,3]#可以看到链表list支持不同元素并存
print(str)
#删除 与del等效
str[1:4]=[]
print(str)


