#奇异值分解
#介绍：有一个矩阵M，可以分解为3个矩阵USV，使得U*S*V等于M。U与V都是正交矩阵（乘以自身的转置矩阵为单位阵），那么S矩阵主对角线上的
#元素成为矩阵M的奇异值，其他元素均为0
#奇异值分解与特征值分解的差别在于，SVD分解能够针对非方阵
#SVD可以用于PCA降维，来做数据压缩和去噪。也可以用于推荐算法，将用户和喜好对应的矩阵做特征分解，进而得到隐含的用户需求来做推荐
import numpy as np
M=np.mat('4 11 14;8 7 -2')
print(M)
U,sv,V=np.linalg.svd(M,full_matrices=False)#full_matrices表示不需要方阵
print('U矩阵：')
print(U)
print('V矩阵：')
print(V)
print('正交性检验：')
print(U*U.T)
print(V*V.T)
print(sv)#sv就是矩阵的特征值


S=np.diag(sv)
print('sv的对角阵：')
print(S)
print('检验USV：还原到原来的矩阵')
print(U*S*V)