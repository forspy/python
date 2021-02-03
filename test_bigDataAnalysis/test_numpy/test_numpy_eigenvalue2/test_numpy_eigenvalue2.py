#提取方阵图片的特征值
import numpy as np
#import scipy.misc as sm
import matplotlib.pyplot as mp
import matplotlib.image as mi
#import imageio
#读取图片数据
#img=sm.imread('./scenery.jpg')#scipy由于版本升级的原因已经没有imread的功能了
#print(img.shape)

img=mp.imread('./scenery.jpg')
#img=imageio.imread('./scenery.jpg')
print(img[0,0],img.shape)#0,0为位置点的像素值，img的shape

r,g,b = [img[:,:,i] for i in range(3)]
#图片灰度算法 Gray = 0.299R+0.587G+0.114*B
img_heat =  0.299*r+0.587*g+0.114*b#形成热成像图
print(img_heat[0][0])

#0-799
#cut_range=np.arange(799,1199)
#img_cut= np.delete(img_heat,cut_range, axis=1)#axis=1为删除列
img_cut=img_heat[::,0:800]#取0:第799列，一共800个

#---------------
#提取img矩阵的特征值与特征向量

img_matix=np.mat(img_cut)#转为矩阵
eigvals,eigvecs=np.linalg.eig(img_matix)#img_matix最好为矩阵对象，只能处理方阵
#---------------

#提取img矩阵的奇异值
img_heat_matrix=np.mat(img_heat)#将img_heat转化为矩阵
U,sv,V=np.linalg.svd(img_heat_matrix,full_matrices=False)#注意img_heat需要为矩阵对象，返回的对象U\sv\V均为矩阵
print(U.shape,sv.shape,V.shape)
img_svd=U*(np.diag(sv))*V#利用svd算出的特征值，逆向推导原矩阵


#抹掉一部分特征值
eigvals[50:]=0
img2=eigvecs*np.diag(eigvals)*eigvecs.I#利用新的特征值回推图片，生成的img2是一个复数矩阵，需要取实部
img2=img2.real#需要取实部

mp.subplot(1,4,1)#原图
mp.imshow(img_heat,cmap='gray')#mp.imshow(img_gray,cmap='jet')为热成像图
mp.xticks([])
mp.yticks([])
mp.subplot(1,4,2)#方阵特征值还原图
mp.imshow(img2,cmap='gray')
mp.xticks([])
mp.yticks([])
mp.subplot(1,4,3)#非方阵svd特征值还原图
mp.imshow(img_svd,cmap='gray')
mp.xticks([])
mp.yticks([])

mp.subplot(1,4,4)#抹去一部分非方阵svd特征值后的还原图
sv_cut=sv
sv_cut[50:]=0


img_svd_new=U*(np.diag(sv_cut))*V
mp.imshow(img_svd_new,cmap='gray')

mp.show()
#img=np.mat(img)