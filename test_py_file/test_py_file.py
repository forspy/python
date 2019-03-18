# python对于文件与流的操作
# python的文件模块导入相当于c/c++的#include<fstream>
import io

# f = open('test.txt')  # 若没有该文件则会抛出FileNotFoundError异常 文件的对象f称为流
# r、w、a为打开文件的基本模式，对应着只读、只写（不存在时创建）、追加模式；
# b、t、+、U这四个字符，与以上的文件打开模式组合使用，二进制模式，文本模式，读写模式、通用换行符，根据实际情况组合使用、
#
# 四、 常见的mode取值组合
# 1、r或rt    默认模式，文本模式读
# 2、rb      二进制文件
# 3、w或wt    文本模式写，打开前文件存储被清空
# 4、wb    二进制写，文件存储同样被清空
# 5、a   追加模式，只能写在文件末尾
# 6、a+  可读写模式，写只能写在文件末尾
# 7、w+ 可读写，与a+的区别是要清空文件内容
# 8、r+   可读写，与a+的区别是可以写到文件任何位置，与w+的区别是可以不清空

# 当你用二进制模式将带有换行符的字符串写入txt文件时，数据存储是正确的，但是当用windows平台的记事本程序打开时，
# 你看到的换行符确实一个个的小黑块，但是，用文本模式，就不存在这样的问题。
# 在这里，涉及到了不同平台由于编码的问题，而对换行符有不同的识别。unix或者linux系统识别\n为换行符的标识，但是windows平台的编码，对\n不予理睬。
# 但是python自身带有转化功能，用文本模式的时候，你不会看到由于平台不同而造成的换行效果不同，但是，二进制模式的时候，
# python便不会再去转化，是什么，就写进去什么，此时的换行符，再用文本模式打开，windows下就不识别‘\n'换行符了。

# 音视频裁剪的时候可以使用rb进行二进制的保存，不使用文本进行自动换行

# sys.stdin, sys.stdout, sys.stderr
# stdin , stdout , 以及stderr 变量包含与标准I/O 流对应的流对象. 如果需要更好地控制输出,而print 不能满足你的要求,
# 它们就是你所需要的. 你也可以替换它们, 这时候你就可以重定向输出和输入到其它设备( device ), 或者以非标准的方式处理它们.

f = open('somefile.txt', 'w')
f.write('hello, ')
f.write('world')
#f.seek(6)#指相对于文件开头进行移动
f.seek(1,0)#0为开头 1为当前 2为末尾
f.write('bob')
f.close()

f1 = open('somefile.txt', 'r')
print(f1.read(6))  # 可指定读几个字符
print(f1.read())  # 会根据文件指针从剩下的字符开始读取
f1.close()


import sys

text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('一共有：', wordcount, '个字')

# 在linux该文件夹下运行
# cat some.txt |python3 test_py_file.py
# |是一个管道 ，|管道将一个命令的输出链接到下一个命令的输入 所以cat的stdout就成为了pyhon3的 stdin

# 也可以使用cat some.txt |sort 对文件按照单词字母大小进行排序


