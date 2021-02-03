#相关性检验--看看相似程度
#使用协方差计算两组统计样本的相关性（相似程度），正值为正相关；负值为负相关，绝对值越大，相关性越好
#计算过程
#A=[a1,a2,...,an]
#B=[b1,b2,...,bn]
#1.平均值
#avg_a=(a1+a2+...+an)/n
#avg_b=(b1+b2+...+bn)/m
#2.离差(距平)---
#dev_a=[a1,a2,a3,...,an]-avg_a
#dev_b=[b1,b2,b3,...,bn]-avg_b
#3.协方差 A的离差*B的离差求平均 cov_ab解释为A相对B的协方差 Cov(x,y)=E[(y-E(x))*(y-E(y))]  E()表示期望=x1*p(x1)+x2*p (x2)+..+xn*p(xn)
#cov_ab=avg(dev_a*dev_b)
import numpy as np
A=np.array([1,2,3])
B=np.array([4,5,6])
avg_a=np.mean(A)
avg_b=np.mean(B)
dev_a=A-avg_a
dev_b=B-avg_b
cov_AB=np.mean(dev_a*dev_b)
print(cov_AB)#0.6666666666666666 正相关  绝对值越大，相关性越好，你涨我也涨，
#由于算出来的协方差绝对值大小没有标准，引入相关系数[-1 1]
#相关系数=协方差cov_ab/(std_a*std_b)标准差的乘积
relatedCov=cov_AB/(np.std(A)*np.std(B))
print(relatedCov)#1.0---表示完全相关


#上述为原理性示范
#---------------------------调用API直接计算
#相关系数矩阵
#[cov_AA cov_AB
# cov_BA cov_BB]
#cov_AA=cov_BB=1
relatedCovMatix=np.corrcoef(A,B)
print(relatedCovMatix)

print(relatedCovMatix[0,1])

#协方差矩阵
#[A的方差 AB的协方差
# BA的协方差 B的方差]
#注：A与A的协方差就是A的方差
covMatix=np.cov(A,B)
print(covMatix)