import numpy as np
import matplotlib.pyplot as mp

mp.figure('polar')
mp.gca(projection='polar')#设置映射方式
mp.title('poalar',fontsize=20)
mp.xlabel(r'$\theta$',fontsize=14)
mp.ylabel(r'$\rho$',fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')


t=np.linspace(0,4*np.pi,1000)#表示角度
r=0.8*t#表示长度
mp.plot(t,r)
mp.show()