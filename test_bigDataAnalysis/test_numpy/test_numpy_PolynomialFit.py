#多项式的一般形式
#y=p0*x^n+p1*x^(n-1)+p2*x^(n-2)+...+pn*x^(n-n)
#多项式拟合的目标是找到一组p0-pn（多项式系数），使得拟合方程尽可能与实际样本相符合
#导函数表示当前函数在摸个位置的走势
import numpy as np
import matplotlib.pyplot as mp
x=np.array([0,1,2,3,4,5])
y=np.array([0,1,4,8,17,26])
n=2#6次以内的多项式拟合较为准确，n过大会过度拟合
num=np.arange(n,-1,-1)#生成系数项

print(num)
p=np.polyfit(x,y,n)
print('多项式系数',p)

Y=np.zeros(y.shape[0])#Y为多项式的拟合值
for i in range(0,x.shape[0]):
    Y[i]=pow(x[i],num).dot(p)#pow(x[i],num)会返回一个幂序列
print('多项式拟合值',Y)
Y1=np.polyval(p,x)
print('API多项式估值',Y1)#封装好的API，用来根据多项式算出Y
#可视化
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
mp.scatter(x,y,label='样本值')
str=str(n)+'次多项式'
mp.plot(x,Y1,label=str)
mp.grid()
mp.legend()


mp.show()
#更多API
#多项式函数求导
#np.polyder(p)
#多项式函数的根
#xs=np.roots(p)
#两个多项式函数差函数
#Q=np.polysub(p1,p2)
#差函数的根就是两个函数的交点
#XS=np.roots(Q)