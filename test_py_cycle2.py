print(range(10))
# 并行迭代
names = ['bob', 'lucy', 'lily']
phones = [123, 456, 789]
for i in range(0, len(names)):
    print(names[i], 'is', phones[i])  # print会自动换行

# zip缝合
# zip缝合联合序列返回一个适合迭代的元组对象序列
for name, phone in zip(names, phones):
    print(name, 'is', phone)
# 查看zip对象可以使用list
print(zip(names, phones))  # <zip object at 0x00000288EA7B8948>
print(list(zip(names, phones)))
# 注：当序列长度不同时，zip将在最短序列用完后停止缝合

string = 'hello world'
print(string.index('el'))
print(string.replace('world', 'friend'))  # 字符串可以使用方法replace替换
array = [1, 2, 3, 4, 5]  # 数组可以按下标直接替换
array[2] = 222
print(array)

# 在未知的大型数组中替换
index = 0
for num in array:
    if (num == 222):
        array[index] = 999
    index += 1  # 需要在for循环中每次对计数器+1
print(array)

# 使用内核函数enumerate()自动计数
listnums = [1, 2, 3, 4, 5, 999]
for count, listnum in enumerate(listnums):
    if (listnum == 999):
        listnums[count] = 6
print(listnums)

# sorted(链表)函数返回一个list
print(sorted([1, 25, 2, 34, 5, 23, 55]))

# 跳出循环
from math import sqrt

for n in range(99, 0, -1):  # for循环会对n进行自动计数
    root = sqrt(n)
    if (root == int(root)):
        print('99-0最大的平方值为：', n)
        break  # 跳出该层循环

# 对比c程序
# #include<iostream>
# using namespace std;
#
# int main()
# {
# 	int array[100];
# 	for(int i=0;i<100;i++)
# 		array[i]=i;
# 	for (int i = 99; i >= 0; i--)
# 		//cout << sqrt(array[i]) << endl;
# 		if (sqrt(array[i])==int(sqrt(array[i])) )
# 		{
# 			cout << "99-0的最大平方值为:" << array[i] << endl;
# 			break;
# 		}
# }

# 从对比中可以看到python省略了
# 1.头文件的加载
# 2.初始化数组的工作，由range完成

# python的解释机制，使得代码更为紧凑，但c/c++代码更为基础和面向底层
