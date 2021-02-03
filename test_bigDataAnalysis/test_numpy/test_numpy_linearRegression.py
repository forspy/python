#线性回归
#最小二乘法
#一元线性预测/多元线性预测
#a*x1+b*y1+c*z3=m1
#a*x2+b*y2+c*z3=m2
#a*x3+b*y3+c*z3=m3

import numpy as np
import matplotlib.pyplot as mp
A=np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
B=np.array([10,20,30])

coefficient=np.linalg.lstsq(A,B,rcond=None)[0]
print(coefficient[0],coefficient[1],coefficient[2])

#构建一个值序列
valueData=np.array([5.31,4.99,3.81,2.11,3.11,3.98,5.43,6.31,7.77,8.65,7.77])

N=3#3天数预测,使用前3天的数据与第四天的值挂勾进行回归预测,经过对N的测试发现6天是比较合理的预测样本长度
row=valueData.shape[0]-N
A=np.zeros((row,N))#如：7行，3列的A
for j in range(row):
    A[j]=valueData[j:j+N]#使用前
B=valueData[N::]
x=np.linalg.lstsq(A,B,rcond=None)[0]#得到回归系数
print(x)
#预测
PreValue=np.zeros(row)
for i in range(row):
    PreValue[i]=(valueData[i:i+N]).dot(x)#将N天的数据与回归系数点乘
print(PreValue)


#-----设置中文
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
time=np.arange(1,valueData.shape[0]+1)
mp.plot(time,valueData,label='实测值')
mp.plot(time[N::],PreValue,label='预测值')
mp.grid()
mp.legend(loc=0)
mp.show()

#对于y=ax+b
#可以对上式简化为
# [x1 1     [k      [y1
#  x2 1   *   =      y2
#  x3 1]     b]      y3]
x=np.array([2,4,6,9])
y=np.array([2,4,6,8])
addedarray=np.ones(x.shape[0])
#A=np.vstack((x,addedarray)).T
A=np.column_stack((x,np.ones_like(x)))#与上面的效果一致np.row_stack 水平合并

print(A)
B=y
coefficient=np.linalg.lstsq(A,B,rcond=None)[0]
print(coefficient)
preValue=np.zeros(x.shape[0])
for i in range(x.shape[0]):
    preValue[i]=coefficient.dot(A[i])
mp.figure('y=kx+b')
mp.scatter(x,y,label='原始数据')
mp.plot(x,preValue,label='拟合值',alpha=0.3)
mp.grid()
mp.legend()
mp.show()