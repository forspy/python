# python的简单数据结构：序列和元组
# 序列是可以修改的，元组不可以
person1 = ['xiaoming', 42]  # 序列#是一种容器
print(person1)
person2 = ['xiaohong', 30]
# 序列可以合并
person3 = [person1, person2]
print(person3)
# 序列的方法
# 1.索引
A = "hello"
print(A[0])
print(A[-1])  # 索引-1代表最后一个字符
# 也可以再input后面使用
# s = input("请输入")[3]  # 第四个为s
# print(s)
B = "hello\
world"  # \ 换行符
print(B)
B = 8 * ['8']  # 可以重复字符串
print(B)

# 下面为一个输出指定年月日的程序
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']  # 表示1-31号
year = input('year:')
month = input('month:')
day = input('day:')
# 这里一定要声明year month day的类型，因为序列的下标是int类型的，而input的默认类型是string
month_name = months[int(month) - 1]  # 表示从months序列里面选择，从0开始
ordinal = day + endings[int(day) - 1]
print(month_name + ' ' + ordinal + ',' + year)

# 2.切片
# 切片可以访问特定范围的元素
tag = "https://github.com/forspy/share"
print(tag[0:19])
number = [1, 2, 3, 4, 5, 6]
print(number[0:2])  # [1,2]表示到2前面的一个数
print(number[-1])  # 6
print(number[-2:-1])  # [5]
print(number[-3:-1])  # [4,5]
print(number[-3:])  # [4,5,6]
print(number[:3])  # [1,2,3]
print(number[:])  # [1,2,3,4,5,6]
