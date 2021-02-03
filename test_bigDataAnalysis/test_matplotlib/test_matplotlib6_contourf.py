#画等高线图
import numpy as np
import matplotlib.pyplot as mp

import matplotlib as mpl
# x:
# 0 1 2
# 0 1 2
# 0 1 2
#
# y:
# 0 0 0
# 1 1 1
# 2 2 2

# -----设置中文
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#生成mesh网格
n=500
x,y=np.meshgrid(np.linspace(-3,3,n),np.linspace(-3,3,n))#表示x从-3到3 y从-3到3的一个mesh网格
#print(x)
#print(y)
z=x**2+y**2

mp.figure('contour')
cntr=mp.contour(x,y,z,8,colors='black',linewidths=1)
#绘制等高线的高度标签文本
mp.clabel(cntr,inline_spacing=1,fmt='%.2f',fontsize=10)#inline_spacing表示数字与线的间距，fmt='%.2f'表示保留小数点后两位

#mp.contourf(x,y,z,8,cmap='jet')#绘制等高线填充图jet映射表示从蓝-红的映射，数值小的是蓝，数值大的是红
mp.imshow(z,cmap='jet',origin='lower')#热成像图,origin='lower'表示y轴向上为正
mp.grid(linestyle=":")
mp.colorbar()
#定制化corlorbar
# cmap = mpl.cm.cool
# norm = mpl.colors.Normalize(vmin=5, vmax=10)
# mp.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
#              cax=ax, orientation='vertical', label='Some Units')
mp.show()
