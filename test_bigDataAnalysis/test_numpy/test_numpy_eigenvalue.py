#特征值与特征向量
#对于n阶方阵A，如果存在数a和非零n维列向量x，使得Ax=ax，则称a是矩阵A的一个特征值，x是矩阵A属于特征值a的特征向量
#eigvals:特征值数组
#eigvecs:特征向量数组
# [1 2 3    [1          [1
#  4 5 6   * 3  = a  *   3
#  7 8 9]    6]          6]
#  方阵A  特征向量x 特征值a 特征向量x
import numpy as np
A=np.mat('1 2 3 4;5 6 7 8;9 10 11 12;13 14 15 16')
print(A)
eigvals,eigvecs=np.linalg.eig(A)#得到4组特征值与特征向量,按列对应
print(eigvals)
print(eigvecs)
#测试-------
a=np.mat('1 2 3 4')
b=np.mat('-0.15115432;-0.34923733;-0.54732033;-0.74540333')
b1=np.mat('-0.15115432;0.72704996;-0.36400894;0.00610215')
print(a*b)#-5.47320329
print(a*b1)#0.23532738#不符，说明特征值与特征向量是按列对应的
print(3.62093727e+01*-0.15115432)#-5.473203108095065
#----------

#逆向推导原矩阵
re_A=eigvecs*np.diag(eigvals)*eigvecs.I#diag表示特征值的对角阵 eigvecs.I表示特征向量的逆矩阵
print(re_A)
eigvals1=eigvals[0]
print(eigvals1)
eigvecs1=eigvecs[:,0]
print(eigvecs1)
A1=eigvecs1*(eigvals1)*(eigvecs1.I)#可见单一特征值还原是不准确的，需要尽可能多的特征值
print(A1)
#---------
