#!user/bin/env python3                            # 1
# coding=gbk                                      # 2
                                                  # 3
# 1.ģ��sys�ܹ����������python������������صı����ͺ���               # 4
# ����ģ�sys.argv                                   # 5
# ����python�ű�ʱ�����ָ��һЩ������Ҳ���������в��� ��Щ����������sys.argv�� ����sys.argv[0]Ϊpython�Ľű���# 6
                                                  # 7
import sys                                        # 8
                                                  # 9
args = sys.argv                                   #10
args.reverse()                                    #11
print(args)                                       #12
                                                  #13
# Ȼ���cmd   ����py�ļ�����Ŀ¼������python test_py_module2_STL.py hello world#14
# ���Կ��� ['world', 'hello', 'test_py_module2_STL.py']#15
                                                  #16
# sys����һЩ��Ҫ�ĺ����ͱ���                                 #17
# sysģ����һЩ��Ҫ�ĺ����ͱ���                                #18
#                                                 #19
# ����/���� ����                                        #20
#                                                 #21
# argv �����в����������ű�����                               #22
#                                                 #23
# exit([arg]) �˳���ǰ���򣬿�ѡ����Ϊ�����ķ���ֵ���ߴ�����Ϣ            #24
#                                                 #25
# modules ӳ��ģ�����ֵ�����ģ����ֵ�                          #26
#                                                 #27
# path ����ģ������Ŀ¼��Ŀ¼���б�                             #28
#                                                 #29
# platform ����sunos5����win32��ƽ̨��ʶ��                  #30
#                                                 #31
# stdin ��׼����������һ�����ļ�����                            #32
#                                                 #33
# stdout ��׼���������һ�����ļ�����                           #34
#                                                 #35
# stderr ��׼����������һ�����ļ�����                           #36
#                                                 #37
# ?                                               #38
#                                                 #39
# ����sys.argv�������ݵ�python�������Ĳ����������ű����ƣ�             #40
#                                                 #41
# ����sys.exit�����˳���ǰ���������try/finally���е��ã�finally�Ӿ��������Ȼ�ᱻִ�У��������ṩһ������������������ʶ�����Ƿ�ɹ����С���unix��һ������������������ʹ�ø�������Ĭ��ֵ�Ϳ����ˣ�Ҳ����0����ʾ�ɹ���������Ҳ�����ṩ�ַ�������������������Ϣ��������û��ҳ�����ֹͣ���е�ԭ�������á�����������ͻ����˳���ʱ���ṩ������Ϣ�ͱ�ʶ��������ʧ�ܵĴ��롣#42
#                                                 #43
# ӳ��sys.modules��ģ����ӳ�䵽ʵ�ʴ��ڵ�ģ���ϣ���ֻӦ����Ŀǰ�����ģ�顣      #44
#                                                 #45
# sys.path��һ���ַ����б������е�ÿ���ַ�������һ��Ŀ¼������import���ִ��ʱ���������ͻ����ЩĿ¼�в���ģ�顣#46
#                                                 #47
# sys.platformģ������ǽ����������������еġ�ƽ̨�����ơ������ǲ���ϵͳ�����֣�Ҳ�����Ǳ�ʶ���������ƽ̨�����������Jython�Ļ�������java�������#48
#                                                 #49
# sys.stdin��sys.stdout��sys.stderrģ����������ļ����������Ǳ�ʾ��׼UNIX�����еı�׼���롢��׼����ͱ�׼����#50
                                                  #51
# 2.os����ϵͳ���� ���ļ�                                 #52
# ����Ҫ����һ��web�����                                   #53
import os                                         #54
                                                  #55
# os.system('/usr/bin/firefox')#linuxд��           #56
####ע��һ��Ҫ��python�ű��Ŀ�ͷд����������                       #57
# !user/bin/env python3                           #58
# coding=gbk                                      #59
# os.system(r'E:/Notepad++/notepad++.exe')  # 'E://Notepad++//notepad++.exe'����Ҳ�� ע������Ȩ�޿��Ƶ�ԭ����ܻ�����#60
                                                  #61
# �����windowsƽ̨�»�����ʹ��Windows���еĺ���                  #62
os.startfile(r'E:\tanzhou\TZKT\TZKT.exe')         #63
                                                  #64
# 3.��web��ҳ                                       #65
# �ڴ���ҳ����webbrowserģ�����                           #66
import webbrowser                                 #67
                                                  #68
webbrowser.open('https://www.baidu.com/')         #69
                                                  #70
#����������һ�����ļ��������кŵĽű�                               #71
import fileinput                                  #72
for line in fileinput.input(inplace=True):        #73
    line=line.rstrip()                            #74
    num=fileinput.lineno()                        #75
    print('{:<50}#{:2d}'.format(line,num))        #76
