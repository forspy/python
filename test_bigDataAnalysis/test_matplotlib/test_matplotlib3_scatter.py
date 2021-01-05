import numpy as np
import matplotlib.pyplot as mp

#-----设置中文
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

n=100
x=np.random.normal(172,20,n)#生成正泰分布的随机数 172期望值 20 标准差 n数字生成数量
y=np.random.normal(60,10,n)

mp.figure('scatter',facecolor='lightgray')#窗口标题，背景颜色
mp.title('scatter')
mp.scatter(x,y,label='Person',c=y,cmap='jet')
mp.grid()
mp.xlabel('身高',fontsize=10)
mp.ylabel('体重',fontsize=10)
mp.legend(loc=1)


#以某种颜色自动填充封闭区域
x=np.linspace(-np.pi,np.pi,1000)
sinx=np.sin(x)
cosx=np.cos(x)
mp.figure()
mp.plot(x,sinx,label=r'$y=sin(x)$')
mp.plot(x,cosx,label=r'$y=cos(x)$')
mp.fill_between(x,sinx,cosx,sinx>cosx,color='r',alpha=0.2)
mp.fill_between(x,sinx,cosx,sinx<=cosx,color='b',alpha=0.2)
mp.xlabel('x轴',fontsize=10)
mp.ylabel('y轴',fontsize=10)
mp.legend()
mp.show()