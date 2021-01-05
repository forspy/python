import numpy as np
import matplotlib.pyplot as mp
x=np.arange(1,11)
y=np.arange(1,11)
y1=np.sin(x)
mp.plot(x,y)
mp.plot(x,y1)
#绘制垂直线
mp.vlines(3,0,10)#x的位置，y0起始，y1结束
#绘制水平线
mp.hlines([1,2,3,4],0,10)#y的位置，x0起始，x1结束
#显示图表
mp.show()#阻塞式窗口
