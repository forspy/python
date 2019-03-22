# 模块urllib通过网络访问文件，就像这些文件位于你的计算机中一样 可用于下载网页、从中提取信息并自动生成研究报告
# urllib2更好一些 对于简单的下载urllib绰绰有余，如果需要实现HTTP身份验证或Cookie,抑或编写扩展来处理

# 打开远程文件
from urllib.request import urlopen

webpage = urlopen(
    'https://www.python.org/')  # 1.使用urlopen打开这个网页文件 2.变量webpage将包含一个类似于文件的对象，这个对象与网页https://www.python.org/相关联
# 也可访问本地文件 例如: file:E:\\python code\\test_py_Socket
# urlopen返回的类似于文件的对象支持方法close、read、readline、readlines，这也是python网页爬虫的基础

text = webpage.read()  # 这拿到的是html格式的文本
print(text)
# 结合正则表达式进行爬虫
import re

m = re.search('(doc[a-z]*)', text.decode())  # 进行所有包含doc的字符串匹配
print(m.group(1))

# 获取远程文件
from urllib.request import urlretrieve

urlretrieve('https://www.python.org/', r'E:\python code\test_py_Socket\python_webpage.html')  # 将网页保存为本地html文件
urlretrieve(r'file:E:\python code\test_py_Socket\test.txt',r'E:\python code\test_py_Socket\test1.txt')#将本地或服务器文件下载保存