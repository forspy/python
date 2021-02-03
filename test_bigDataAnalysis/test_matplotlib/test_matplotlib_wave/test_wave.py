import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as mdates
import pandas as pd

#-----设置中文
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#grid=mp.GridSpec(2,3)#grid = plt.GridSpec(2, 3, wspace=0.5, hspace=0.5)设置多个字窗口
grid = mp.GridSpec(2, 3, wspace=0.1, hspace=0.1)#设置多个字窗口
mp.subplot(grid[0:2,0:2])
data_cj=pd.read_excel('波浪202012.xls',sheet_name='预警2号')#取长江口外海波高数据
#print(data.shape)
#print(data['时间'],data['有效波高(m)'])
#长江口外海波高
t_cj=data_cj['时间']
wave_cj=data_cj['有效波高(m)']
wave_cj[wave_cj==99999]=np.nan
#mp.scatter(data['时间'][::5],data['有效波高(m)'][::5],label='长江口外海有效波高')
stdwave_cj=np.round(np.std(wave_cj),2)#计算标准差，并保留两位小数
mp.plot(t_cj,wave_cj,linestyle='--',alpha=0.8,label='长江口外海波高'+'(标准差'+str(stdwave_cj)+')')
#mp.xlim([dt.datetime(2020, 12, 1), dt.datetime(2020, 12, 31)])  # 日期上下限
mp.xlabel('时间',fontsize=10)
mp.ylabel('波高/m',fontsize=10)
print(np.argmax(wave_cj),t_cj[np.argmax(wave_cj)],np.max(wave_cj))#返回最大值位置
mp.scatter(t_cj[np.argmax(wave_cj)],np.max(wave_cj),label='长江口海外最大波高')#最大波高点
mp.text(t_cj[np.argmax(wave_cj)],np.max(wave_cj),str(np.max(wave_cj))+'巨浪',va='bottom',color='blue')
#绘制平均线
#print(np.nanmean(a))#np.nansum(a)去除nan求平均
wave_cj_mean=np.round(np.nanmean(wave_cj),2)
mp.hlines(wave_cj_mean,t_cj[0],t_cj[len(t_cj)-1],linestyle='--',alpha=0.2,label='长江口外海平均波高('+str(wave_cj_mean)+'m)')
# mean=np.mean(data1)
#



#subplot
#杭州湾波高
data_hzw=pd.read_excel('波浪202012.xls',sheet_name='预警3号')#取长江口外海波高数据
t_hzw=data_hzw['时间']
wave_hzw=data_hzw['有效波高(m)']
wave_hzw[wave_hzw==99999]=np.nan
stdwave_hzw=np.round(np.std(wave_hzw),2)#保留两位小数
mp.plot(t_hzw,wave_hzw,linestyle='-',alpha=0.5,label='杭州湾奉贤海域波高'+'(标准差'+str(stdwave_hzw)+')')
mp.scatter(t_hzw[np.argmax(wave_hzw)],np.max(wave_hzw),label='杭州湾奉贤海域最大波高')#最大波高点
mp.text(t_hzw[np.argmax(wave_hzw)],np.max(wave_hzw),str(np.max(wave_hzw))+'中浪',va='bottom',color='orange')
wave_hzw_mean=np.round(np.nanmean(wave_hzw),2)
mp.hlines(wave_hzw_mean,t_hzw[0],t_hzw[len(t_hzw)-1],colors='orange',alpha=0.2,label='杭州湾奉贤海域平均波高('+str(wave_hzw_mean)+'m)')

mp.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))#设置横坐标格式

lst = np.array([1, 3,np.nan,4, 5])
print(np.sum(lst>=1),np.sum(~np.isnan(lst)),len(lst),np.shape(lst))#np中指定条件的长度，非Nan的个数，序列长度,维度
mp.legend()
mp.grid()

# mp.subplot(grid[0:1,2:3])
# values = [26, 17, 21, 29, 11]#占比
# spaces = [0.05, 0.01, 0.01, 0.01, 0.01]#扇形之间的间距
# labels=['python','JavaScript','C++','Java','PHP']
# colors=['dodgerblue','orangered','limegreen','violet','gold']
# mp.pie(values,spaces,labels,colors,'%.2f%%',shadow=True,startangle=0,radius=1)
# mp.axis('equal')#圆形

#统计长江口外海海浪浪型分布
mp.subplot(grid[0:1,2:3])
labels = ['巨浪', '大浪', '中浪', '轻浪及以下']

numCount_cj=np.sum(~np.isnan(wave_cj))
#test_bool=(True,True) and (False,False)#普通逻辑运算
#test_bool=np.logical_and(wave_cj>=4.0,wave_cj<=6.0)#numpy特有的逻辑运算

size_cj_julang=np.sum(np.logical_and(wave_cj>=4.0,wave_cj<=6.0))/numCount_cj*100#巨浪占比
sizes_cj_dalang=np.sum(np.logical_and(wave_cj>=2.5,wave_cj<4.0))/numCount_cj*100#大浪占比
sizes_cj_zhonglang=np.sum(np.logical_and(wave_cj>=1.25,wave_cj<2.5))/numCount_cj*100#中浪占比
size_cj_xiaoqinlang=np.sum(wave_cj<1.25)/numCount_cj*100#轻浪以下
sizes = [size_cj_julang, sizes_cj_dalang, sizes_cj_zhonglang, size_cj_xiaoqinlang]
explode = (0.1, 0.2, 0.1, 0.1) # 只爆炸第二块饼，爆炸距离是半径的0.1。

#mp.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%', pctdistance=0.7, shadow=True, startangle=90)
mp.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%', pctdistance=0.7,  shadow=True, startangle=90,
        counterclock=False, wedgeprops=dict(edgecolor='w', width=0.7, linewidth=5))
mp.axis('equal') # 等价于 ax1.set(aspect='euqal')，使得饼图在figure窗口放大缩小的过程中，保持圆形不变。
mp.title('长江口外海浪级比例')

#杭州湾浪型分布
mp.subplot(grid[1:2,2:3])
labels = ['中浪', '轻浪及以下']

numCount_hzw=np.sum(~np.isnan(wave_hzw))
#test_bool=(True,True) and (False,False)#普通逻辑运算
#test_bool=np.logical_and(wave_cj>=4.0,wave_cj<=6.0)#numpy特有的逻辑运算

size_hzw_zhonglang=np.sum(np.logical_and(wave_hzw>=1.25,wave_hzw<=2.5))/numCount_hzw*100#中浪占比
sizes_cj_qinglang=np.sum(wave_cj<1.25)/numCount_hzw*100#轻浪占比

sizes = [size_hzw_zhonglang, sizes_cj_qinglang]
explode = (0.1, 0.1) # 只爆炸第1块饼，爆炸距离是半径的0.1。

#mp.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%', pctdistance=0.7, shadow=True, startangle=90)
mp.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%', pctdistance=0.7,  shadow=True, startangle=90,
        counterclock=False, wedgeprops=dict(edgecolor='w', width=0.7, linewidth=5))
mp.axis('equal') # 等价于 ax1.set(aspect='euqal')，使得饼图在figure窗口放大缩小的过程中，保持圆形不变。
mp.title('杭州湾奉贤海域浪级比例',y=-0.2)#标题放在下面


mp.show()