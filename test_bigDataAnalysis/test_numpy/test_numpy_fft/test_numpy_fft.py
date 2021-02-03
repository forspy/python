#快速傅里叶变换模块（fft）
#法国科学家傅里叶提出，任何一条周期曲线，无论多么跳跃或不规则，都能表示成一组光滑正弦曲线叠加之和
#可将时域上的信号转化为频域上的信号，减少信号的储存量
#f(t)=Asin(wt+φ)#A振幅，w频率，φ相位

#傅里叶变化的功能就是得到一组A振幅，w频率，φ相位

#采样数量代表一段波的y的个数，采样周期代表相邻两个点的时间间隔



#先构造一个方波
import matplotlib.pyplot as mp
import numpy as np
import numpy.fft as nf
x=np.linspace(-2*np.pi,2*np.pi,1000)
y=np.zeros(1000)
n=1000
#方波由一组y=4pi/(2n-1)*sin((2n-1)x)的正弦波叠加而成
for i in range(1,n+1):#表示i从1到n
    y_=4*np.pi/((2*i-1))*np.sin((2*i-1)*x)#每个y_都是一个正弦函数
    y+=y_#累加的y就是方波

complex_array=nf.fft(y)#拆解一个复数，表征A与φ,复数的模代表A，复数的辐角代表初相位

y_re=nf.ifft(complex_array)#
#y_re_abs=np.abs(y_re)
mp.subplot(1,2,1)
mp.plot(x,y,label='y',color='black')
mp.plot(x,y_re,label='ifft',linewidth=6,alpha=0.2)


mp.subplot(1,2,2)
#为了滤波，先绘制频域图像
#水平轴表示频率，垂直轴表示能量
#freqs=nf.fftfreq(采样数量，采样周期)
freqs=nf.fftfreq(y.size,x[1]-x[0])#频率数组
pows=np.abs(complex_array)#能量数组
#线代的核心理念就是批量操作
mp.plot(freqs[freqs>0],pows[freqs>0],label='freqFigure')#选择频率大于0的部分绘制


mp.legend()
mp.show()
