# 模块re 提供了对正则表达式的支持
# 正则表达式是文本片段匹配
# 1.通配符
# '.ython'与'python'、'cython'、'jython'等都匹配,但不与'ython'、'ccython'等长度不一的匹配
# 2.对特殊字符进行转义
# 要使得'baidu.com'中的'.'不进行通配，需要这样设置'baidu\\.com'也可以r'baidu\.com'也可以'baidu\.com'
# 3.字符集匹配
# '[pj]thon'与'python'和'jython'都匹配，'[a-z]'与a~z的字母都匹配 ，'[^abc]'与除了a、b、c以外的任何字母都匹配
# 4.管道模式
# 只想匹配两个字符串 可以'python|perl' 也可以简写为'p(ython|erl)'
# 5.扩大搜索范围 可包含，可不包含
# r'(http://)?(www\.)?python\.org' 与下面的几种情况匹配
# 'http://www.python.org'
# 'http://python.org'
# 'www.python.org'
# 'python.org'
# a.正则搜索
import re

if re.search('hello', 'hi hello world'):  # 进行整段匹配
    print('found')
else:
    print('not found')

if re.match('hello', 'hi hello world'):  # 只检测开头，开头不匹配则返回false
    print('found')
else:
    print('not found')

# b.正则分割
text = 'bob,,,lily   lucy,jim'
print(re.split('[, ]+', text))  # +表示模式可重复多次 []里面既有逗号也有空格

# 要找出字符串内包含的所有单词
pat = '[a-zA-Z]+'
text1 = "are you OK?are you,thank you!thank you very much!I'm a mfan.Do you like me?thank you very much"
print(set(re.findall(pat, text1)))  # 这里可以使用set对重复的单词去重

# c.正则替换
pat2 = 'world'
text2 = 'hello world'
print(re.sub(pat2, 'bob', text2))

# d.正则转义
# 有的时候有大量. 而你不想花时间去\\.
print(re.escape('www.baidu.com'))
if re.search('baidu\.com', 'www.baidu.com'):  # 进行整段匹配
    print('found')
if re.search(re.escape('baidu.com'), 'www.baidu.com'):  # 进行整段匹配
    print('found')

# python re模块正则表达式为python的爬虫打下了基础

# 关键信息的提取
t = 'From:       Shang hai<>\n'
import fileinput

pat = re.compile('From:( *)?(.*)<>$')  # *表示可重复0，1或多次 这里面的技巧有（ *）?表示from后面可以有任意数量的空格 当然这样需要把编组group调整为2
m = pat.match(t)
if m:
    print(m.group(2))
# 以下需要在cmd终端中传入参数
pat = re.compile('From:( *)?(.*)$')  # *表示可重复0，1或多次 $表示匹配到文本
for line in fileinput.input():
    # print(line)
    m = pat.match(line)
    if m: print(m.group(2))  # group(1)表示编组

# 需要在cmd里面传入参数
# python test_py_module5_Regular_expression.py message.txt
# 注意文件名中最好不要有空格
