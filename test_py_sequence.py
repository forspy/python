# 数组和字符串都是序列，可使用序列相加的功能
num1 = [1, 2, 3]
num2 = [4, 5, 6]
num3 = num1 + num2
print(num3)
# 字符串也可相加
print('abc' + 'def')
# 序列乘法
print('abc' * 5)
print(num1 * 2)
# python可以使用0初始化，也可以使用none，表示没有
sequence = [None] * 10
print(sequence)
# in 运算符的用法 搜索字符串
permission = 'rw'
bool_value = 'w' in permission
print(bool_value)  # 返回true
bool_value = 'ww' in permission
print(bool_value)  # 返回false

# 示例：检查账户密码
database = [
    ['forspy', '1234'],  # 注意密码也要写成字符串形式，因为input得到的是字符串
    ['invoker', '3.1415926']
]
username = input('accout:')
password = input('password:')
if [username, password] in database: print('access!')

# 长度len 最小值min 最大值 max
numbers = [100, 34, 678]
print(len(numbers))
print(min(numbers))
print(max(numbers))
print(min(1,2,3,4))
