import numpy as np
import matplotlib.pyplot as mp

# -----设置中文
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

mp.figure('Bar')
monthX = np.arange(1, 13)*2
apples = np.array([10, 11, 12, 30, 50, 22, 19, 51, 53, 66, 90, 100])
oranges = np.array([12, 34, 33, 20, 50, 11, 89, 30, 21, 45, 50,70])
mp.bar(monthX-0.4, apples,0.8, color='dodgerblue', label='Apple')#减去0.2的目的是为了与下一个柱状图分开,0.8表示宽度(默认0.8)
#添加柱状图上的数字
for m,n in zip(monthX,apples):
    mp.text(m-0.8,n,n,va='bottom')
for (m,n) in zip(monthX,oranges):
    mp.text(m+0.1,n,n,va='bottom')
mp.bar(monthX+0.4,oranges,0.8,color='orangered',label='Orange')
mp.xticks(monthX, ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'])
mp.xlabel('月份')
mp.ylabel('')
mp.legend()
mp.grid(linestyle=":")
mp.show()
