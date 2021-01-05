# python 中 false None 0 "" () [] {} 都被视为假
name = input("what's your name?:")
if (name.endswith('b')):  # python的语法是在if条件句后面加:
    print('yes')
else:
    print('no')
# c版本的三目运算在python中的语法
status = 'yes' if name.endswith('b') else 'no'

num = int(input('enter a number:'))  # 需要强转为int
if (num > 0):
    print('>0')
elif (num == 0):
    print('=0')
else:
    print('<0')

# == 和is
# ==用来检查值
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
# is 用来检查对象
print(x is y)

name = input('name?:')
if ('s') in name:
    print('yes')
else:
    print('no')

# 字母顺序
print('a' > 'A')

# 逻辑运算符 and or not
# 注：短路逻辑，如果A and B，A为false 则不判断B立刻返回false

# python 的断言检查
age = 10
assert (age < 100)  # 断言，即不满足则发生断言失败，程序抛出异常


while True:
    name=input("请输入")

#asd
print('ss')