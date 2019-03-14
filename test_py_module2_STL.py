#!user/bin/env python3                            # 1
# coding=gbk                                      # 2
                                                  # 3
# 1.模块sys能够让你访问与python解释器紧密相关的变量和函数               # 4
# 最常见的，sys.argv                                   # 5
# 调用python脚本时你可能指定一些参数，也就是命令行参数 这些参数将放在sys.argv中 其中sys.argv[0]为python的脚本名# 6
                                                  # 7
import sys                                        # 8
                                                  # 9
args = sys.argv                                   #10
args.reverse()                                    #11
print(args)                                       #12
                                                  #13
# 然后打开cmd   进入py文件所在目录，输入python test_py_module2_STL.py hello world#14
# 可以看到 ['world', 'hello', 'test_py_module2_STL.py']#15
                                                  #16
# sys里面一些重要的函数和变量                                 #17
# sys模块中一些重要的函数和变量                                #18
#                                                 #19
# 函数/变量 描述                                        #20
#                                                 #21
# argv 命令行参数，包括脚本名称                               #22
#                                                 #23
# exit([arg]) 退出当前程序，可选参数为给定的返回值或者错误信息            #24
#                                                 #25
# modules 映射模块名字到载入模块的字典                          #26
#                                                 #27
# path 查找模块所在目录的目录名列表                             #28
#                                                 #29
# platform 类似sunos5或者win32的平台标识符                  #30
#                                                 #31
# stdin 标准输入流——一个类文件对象                            #32
#                                                 #33
# stdout 标准输出流——一个类文件对象                           #34
#                                                 #35
# stderr 标准错误流——一个类文件对象                           #36
#                                                 #37
# ?                                               #38
#                                                 #39
# 变量sys.argv包括传递到python解释器的参数，包括脚本名称；             #40
#                                                 #41
# 函数sys.exit可以退出当前程序（如果在try/finally块中调用，finally子句的内容仍然会被执行）。可以提供一个整数参数，用来标识程序是否成功运行——unix的一个惯例。大多数情况下使用该整数的默认值就可以了（也就是0，表示成功）。或者也可以提供字符串参数，用作错误信息，这对于用户找出程序停止运行的原因会很有用。这样，程序就会在退出的时候提供错误信息和标识程序运行失败的代码。#42
#                                                 #43
# 映射sys.modules将模块名映射到实际存在的模块上，它只应用于目前导入的模块。      #44
#                                                 #45
# sys.path是一个字符串列表，其中的每个字符串都是一个目录名，在import语句执行时，解释器就会从这些目录中查找模块。#46
#                                                 #47
# sys.platform模块变量是解释器正在其上运行的“平台”名称。可能是操作系统的名字，也可能是标识其他种类的平台，如果你运行Jython的话，就是java虚拟机。#48
#                                                 #49
# sys.stdin、sys.stdout、sys.stderr模块变量是类文件流对象。它们表示标准UNIX概念中的标准输入、标准输出和标准错误。#50
                                                  #51
# 2.os操作系统命令 打开文件                                 #52
# 例如要启动一个web浏览器                                   #53
import os                                         #54
                                                  #55
# os.system('/usr/bin/firefox')#linux写法           #56
####注意一定要在python脚本的开头写上下面两句                       #57
# !user/bin/env python3                           #58
# coding=gbk                                      #59
# os.system(r'E:/Notepad++/notepad++.exe')  # 'E://Notepad++//notepad++.exe'这样也行 注意受于权限控制的原因可能会阻塞#60
                                                  #61
# 如果在windows平台下还可以使用Windows特有的函数                  #62
os.startfile(r'E:\tanzhou\TZKT\TZKT.exe')         #63
                                                  #64
# 3.打开web网页                                       #65
# 在打开网页方面webbrowser模块更加                           #66
import webbrowser                                 #67
                                                  #68
webbrowser.open('https://www.baidu.com/')         #69
                                                  #70
#下面来考虑一个在文件中添加行号的脚本                               #71
import fileinput                                  #72
for line in fileinput.input(inplace=True):        #73
    line=line.rstrip()                            #74
    num=fileinput.lineno()                        #75
    print('{:<50}#{:2d}'.format(line,num))        #76

