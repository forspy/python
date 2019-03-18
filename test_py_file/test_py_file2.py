# 更加实用的python读取手段
f = open('some.txt', 'r')
t = f.readline()  # 只读一行
print(t)
print(f.readline())
f.close()
# 对于多个客户端访问一个数据文件时，如果说这个文件正在被写入，那么客户端就有可能读取到错误的文件，甚至根本读不到文件的数据
# 对于服务器正在修改的文件可以使用flush将缓存刷入到文件中，并且flush的功能可以禁止在刷入过程中其他程序访问这个文件，刷完之后使用.close()关闭这个文件流，就可以继续共享
# 要确保文件得以关闭可以使用
# try:
#     #将数据写入到文件中
# finally:
#     file.close()
#
# #python为这个结构设计了一条语句
# with open('somefile.txt') as somefile:
#     func(somefile)
# #在func结束后会自动close文件，即使出现异常

# 那么我们想要修改其中的一行应该怎么办呢？
f1 = open('some.txt', 'r')
lines = f1.readlines()
f1.close()
lines[1] = 'mom\n'
f2 = open('some.txt', 'w')
f2.writelines(lines)
f2.close()

f3 = open('some.txt', 'r')
print(f3.read())
f3.close()

#如果想在文本上添加文字
def process(string):
    print('add:',string)

ff=open('test.txt')

while True:
    line=ff.readline()
    if not line:break
    process(line)

ff.close()

#在文件不大的情况下
with open('test.txt') as f:
    for char in f.read():
        process(char)#逐个单词添加

