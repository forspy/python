import numpy as np

a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
print(a)
print(b)
print('---------------')
verticalAB = np.vstack((a, b))#上下拼接
print(verticalAB)
a1,b1=np.vsplit(verticalAB,2)#上下拆成两个数组
print(a1)
print(b1)
print('---------------')
horizontalAB=np.hstack((a,b))#左右拼接
print(horizontalAB)
a2,b2=np.hsplit(horizontalAB,2)#左右拆成两个数组
print(a2)
print(b2)
print('---------------')
deepAB=np.dstack((a,b))
print(deepAB)
#a3,b3=np.dsplit(deepAB,2)
#print(a3)
#print(b3)
print('--------------')
#------------------长度不等数据组合
data1=np.array([1,2,3,4,5])
data2=np.array([6,7,8,9])
#补充data2数组使其与date1纬度相同
data2=np.pad(data2,pad_width=(0,1),mode='constant',constant_values=10)#前面补0个元素，后面补1个元素，补-1
print(data2)
print('-------')
verticalData=np.vstack((data1,data2))
print(verticalData)

