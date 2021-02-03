import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as mdates
import pandas as pd

#-----设置中文
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data_cj=pd.read_excel('水温202012.xls',sheet_name='预警2号')#取长江口外海波高数据

t_cj=data_cj['时间']
SST_cj=data_cj['水温(℃)']
SST_cj[SST_cj==99999]=np.nan

mp.plot(t_cj,SST_cj,linestyle='--',alpha=0.8,label='长江口及周边海域SST')
mp.xlabel('时间',fontsize=10)
mp.ylabel('温度/℃',fontsize=10)
#绘制平均线
#print(np.nanmean(a))#np.nansum(a)去除nan求平均
SST_cj_mean=np.round(np.nanmean(SST_cj),1)
mp.hlines(SST_cj_mean,t_cj[0],t_cj[len(t_cj)-1],linestyle='-',alpha=0.2,label='平均SST'+'('+str(SST_cj_mean)+'℃)')


mp.legend()
mp.grid()
mp.show()