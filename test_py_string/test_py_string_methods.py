# center方法 让字符串居中
str2 = "hello world"
print("hello world".center(25, "*"))
# 查找字符串
print(str2.find("ld"))  # 从0位置开始 没有找到返回-1

# join字符串链表合并,必须同为字符类型
add = '+'
seq = ['1', '2', '3', '4', '5']
print(add.join(seq))  # 注意这是.join()的返回结果，而不是改变add，所以需要直接用print输出
dir = [" ", "usr", "bin", "env"]
print("/".join(dir))
print('c:' + '\\'.join(dir))  # 这里推荐使用''

# lower返回小写
print('ABS'.lower())

# title首字母大写
print('we are family'.title())

#replace替换
str1='we are family'
print(str1.replace('family','friend'))#需要直接用print接住

#split将字符串拆分为序列
print('1+2+3+4+5'.split('+'))

#strip除去字符串开头和末尾的空白,可用于账户名的比对
print('  hello world!  '.split())

#translate替换所有字母
table=str.maketrans('l','k')#1.先建立转换表
print('hello world'.translate(table))#2.替换

#判断字符是否满足特定条件
#isanum isalpha isdigit islower。。。
