#fft滤波
import numpy as np
import numpy.fft as nf
import matplotlib.pyplot as mp
import scipy.io.wavfile as wf

sample_rate,sigs=wf.read('./Hummingbird-1track.wav')#目前好像只能读取.wav文件  sample_rate代表采样点数/每秒   sigs代表采样位移y（单声道）
print(sample_rate,sigs.shape)#22050个点,
#绘制音频时域图
mp.subplot(3,2,1)
print(len(sigs))#一共有几个采样位移
times=np.arange(len(sigs))/sample_rate#表示时域段
mp.xlabel('Time')
mp.ylabel('Signal',fontsize=12)
mp.plot(times,sigs,label='Time Domain')
mp.legend()
mp.grid()

#绘制频域图像
mp.subplot(3,2,2)
freqs=nf.fftfreq(sigs.size,1/sample_rate)#采样点的个数，采样点的周期
print(freqs)
complex_array=nf.fft(sigs)#复数，表示模与辐角
pows=np.abs(complex_array)
mp.ylabel('pow')
mp.xlabel('freq')
mp.semilogy(freqs[freqs>0],pows[freqs>0],label='Frequence Dommain')#使用半对数坐标轴显示高频信号与噪声
mp.grid()
mp.legend()

#去除低能噪声--方式一--只拿最大能量
powmaxFreq=freqs[pows.argmax()]#最大能量对应的频率
#拿到噪声下表
test_noise_indices=np.where(freqs!=powmaxFreq)[0]#找到频率不为最大频率的下标
test_complex_array=complex_array.copy()
test_complex_array[test_noise_indices]=0
test_filter_pows=np.abs(test_complex_array)
#绘制只保留最高能量频率的频域图
mp.subplot(3,2,3)
mp.ylabel('pow')
mp.xlabel('freq')
mp.semilogy(freqs[freqs>0],test_filter_pows[freqs>0],label='Highest Frequence Dommain')#使用半对数坐标轴显示高频信号与噪声
mp.grid()
mp.legend()


#去除低能噪声--方式二--保留10000以上的能量

print('pows:')
print(pows)
#a=np.array([1,2,3,4,5])
#indices=a<3#a必须得是np类型
noise_indices=pows<=1000000#找到能量低于10000的噪声下标
new_complex_array=complex_array.copy()
new_complex_array[noise_indices]=0
filter_pows=np.abs(new_complex_array)
mp.subplot(3,2,4)
#绘制只保留最高能量频率的频域图
mp.ylabel('pow')
mp.xlabel('freq')
mp.semilogy(freqs[freqs>0],filter_pows[freqs>0],label='High Frequence Dommain')#使用半对数坐标轴显示高频信号与噪声
mp.grid()
mp.legend()


#逆向傅里叶变换
mp.subplot(3,2,5)
re_sigs=nf.ifft(new_complex_array)
mp.xlabel('Time')
mp.ylabel('Signal',fontsize=12)
mp.plot(times,re_sigs,label='Re Time Domain')
mp.legend()
mp.grid()
print(np.real(re_sigs))
#abs_re_sigs=np.abs(re_sigs)
int_re_sigs=re_sigs.astype(np.int16)#因为ifft还原出来的是复数，转成int后相当于复数的模（含正负）
#重新生成音频文件
wf.write('./filter3.wav',sample_rate,int_re_sigs)
mp.show()
