# 利用python创建一个斐波那契数列
a = [1, 2, 3, 4, 5]
print(a[-2], a[-1])  # 表示输出a的倒数第二个数和倒数第一个数
# 因此
fibs = [0, 1]
for i in range(0, 8):  # 表示进行8次循环
    fibs.append(fibs[-2] + fibs[-1])  # 每次在尾部增加一个数，该数是链表中的前两个数的和
print(fibs)


# 下面来看一段抽象的应用,需求是计算这个网页中的每个单词的使用频率
def download_page():
    return


def compute_frequencies():
    return


page = download_page()
freqs = compute_frequencies()
# for word, freq in freqs:
# print(word,freq)
print(page, freqs)


# 将具体的某个模块的工作交给某个函数去做，这就是抽象
# python的函数定义
def fibs_func(num):
    '设置一个斐波那契数列'  # python特有的函数文档，写入函数体中用于说明
    result = [0, 1]
    for j in range(0, num - 2):
        result.append(result[-2] + result[-1])
    return result


fibs = fibs_func(10)
print(fibs)

# print(fibs_func.__doc__)#显示说明
# print(help(fibs_func))#显示说明和代码段位置

# 注意python的所有函数都必须设return ，有对象返回对象 没有对象返回None

# 函数的作用域问题
names = ['lily', 'bob']
n = names
n[0] = 'lucy'
print(names)  # 发现改变了链表的值，因为names和n都指向这个链表

nn = names[:]  # 表示取得是链表的切片，会进行深拷贝
print(n is names)
print(nn is names)
print(nn == names)

# 现在修改nn将不会对names产生影响
nn[0] = 'Tim'
print(names)
