import numpy as np
import matplotlib.pyplot as mp
#-----设置中文
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# 生成正弦曲线
x = np.linspace(0, 2 * np.pi, 1000)
print(x.shape)
sinx = np.sin(x)
ax=mp.gca()#获取坐标轴对象
#ax.set_xlabel(r'X 轴',fontsize=10) #设置x轴名称
#ax.set_ylabel(r'Y 轴',fontsize=10) #设置y轴名称
mp.xlabel('X 轴')
mp.ylabel('Y 轴')
#ax.spines['bottom'].set_positon(0)
mp.plot(x, sinx, linestyle='-.', linewidth=1, color='r', alpha=0.5,label=r'$y=sin(x)$')  # alpha表示透明度 线型‘-’、‘--’、‘-.’、‘:’
mp.xlim(0, 5)
mp.ylim(-1, 1)
# 刻度
mp.xticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],['-π',r'$-\frac{\pi}{2}$','0','π/2','π'])#LaTex排版语法
mp.title('函数')
mp.grid()#可以查询’python设置网格刻度线‘
mp.legend()


#画cos(x)
mp.figure()#会创建一个新的窗口
cosx=np.cos(x)
mp.scatter(x,cosx,marker='.',s=1,color='b',label=r'$y=cos(x)$')#maker=./o zorder=3图层顺序
#刻度特殊语法
#r'$x^n+y^n=z^n$'
#r'$\int\frac{1}{x}dx=\ln|x|+C$' 表示积分
#搜索Latex公式语法
#设置坐标轴
mp.legend(loc=1)#表示右上角，不填为最佳位置，2为左上角
mp.tight_layout()#设置紧凑布局

mp.show()
