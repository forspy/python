import numpy as np

a = np.arange(1, 10)  # [1 2 3 4 5 6 7 8 9]
print(a)
print(a[:3])  # [1 2 3]
print(a[3:6])  # [4 5 6]
print(a[6:])  # [7 8 9]
print(a[::])  # [1 2 3 4 5 6 7 8 9]
print(a[::2])  # [1 3 5 7 9]
print(a[::-1])  # [9 8 7 6 5 4 3 2 1]
print(a[2::3])  # [3 6 9]
print('------------')
# 切片维度
a = np.arange(1, 28)
a.shape = (3, 3, 3)
print(a)
print('-------------')
print(a[0, :, :])  # 切出第0页
print('---------')

a = np.arange(1, 28).reshape(3, 3, 3)
print(a[0, 0:2, 0:3])  # 第0页的，2行3列
# np的数组掩码操作,类似于matlab里面的find()函数
#数组的查找与定位
a = np.arange(3) # [0 1 2]
mask = [True, True, False]
maskBool = a < 2
print(maskBool)
print(a[mask], a[maskBool])
#将不符合的数据替换掉
print('--------------------')
a = np.arange(9).astype('float')
print(a[(a % 2 == 0)])
maskBool = a < 6
print(maskBool)
count=0#加一个位置计数
for iBool in maskBool:
    if iBool==False:
        a[count]=np.nan
    count+=1
print(a)
print('----------------------')

#按位置重新排列
aryTest=np.array(['a','b','c','d'])
mask=[3,0,0,1,1,2]
print(aryTest[mask])

#array中数组元素的索引位置

a=np.arange(1,10).reshape(3,3)
index=np.argwhere(a>5)
print(index)
#--------------
for (i,j) in index:
    print(a[i][j])
#--------------


