#插值
import scipy.interpolate as si
import numpy as np
import matplotlib.pyplot as mp
#找一组散点坐标
min_x=-50
max_x=50
dis_x=np.linspace(min_x,max_x,20)
dis_y=np.sinc(dis_x)
mp.subplot(1,3,1)
mp.scatter(dis_x,dis_y,label='dispersed')

#使用插值，使散列的点连续化
funcLinear=si.interp1d(dis_x,dis_y,kind='linear')#返回的linear实际上是一个函数f(x)
x=np.linspace(min_x,max_x,1000)
y=funcLinear(x)
mp.subplot(1,3,2)
mp.plot(x,y,label='linear interped')

#三次样条插值
funcCubic=si.interp1d(dis_x,dis_y,kind='cubic')#返回的linear实际上是一个函数f(x)
x=np.linspace(min_x,max_x,1000)
y=funcCubic(x)
mp.subplot(1,3,3)
mp.plot(x,y,label='cubic interped')
mp.show()