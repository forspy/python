# 作用域与全局变量
a_external = 10


def func(param):
    a_external = param  # 这样全局变量并不会被改变(此处不同于c)
    return


func(11)
print(a_external)


def func1(param):
    globals()['a_external'] = param  # globals()['a_external']以字典的方式找到了全局变量的内存，因而可以改变全局变量(局部变量使用locals())
    return


func1(11)
print(a_external)


def func2(param):
    global a_external  # 方法二，明确地指出这是一个全局变量
    a_external = param
    return


func2(111)
print(a_external)


# python地函数嵌套，目前不使用，待用时学习

# 递归--调用自身
# 递归由两部分组成：
# 基线条件：满足条件时返回一个值
# 递归条件：解决递推问题

# 实例1：阶乘
def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


print(factorial(5))


# 递归阶乘方法An=n*An-1
def factorial_rec(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial_rec(5))


# 同理幂函数
def power(x, n):
    result = 1
    for i in range(0, n):
        result *= x
    return result


print(power(2, 3))


def power_rec(x, n):
    if (n == 0):
        return 1
    else:
        return x * power_rec(x, n - 1)


print(power_rec(2, 3))


# 递归实现二分法查找,要求有序
def binSearch(list, target_num, lower=0, upper=None):
    if (upper is None):
        upper = len(list) - 1
    if lower == upper:
        if (target_num == list[lower]):
            print('在第{}位置找到{}'.format(lower, target_num))
        else:
            print('没有找到')
        return upper
    else:
        middle = (lower + upper) // 2
        if list[middle] < target_num:
            return binSearch(list, target_num, middle + 1, upper)
        else:
            return binSearch(list, target_num, lower, middle)  # 因为是包含大于和等于，所以不需要对middle-1了，等于地时候直接lower=upper


list = [1, 2, 4, 6, 7, 9, 12, 15]
print(binSearch(list, 12))


# # 补充filter函数返回真值条件下地元素
# def func(x):
#     return x.isalnum()
#
#
# seq = ["foo", "x41", "?!"]
# a = list(filter(func, seq))
# print(a)
