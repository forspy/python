# numpy的核心 多维数组
# 代码简洁，减少python代码中的循环
# 底层实现：C+python 保证性能

import numpy as np

ary = np.array([1, 2, 3, 4, 5, 6])
print(type(ary))
print(ary.shape)  # (6,)是一个元组
#构建np类型的二维数组
ary1 = np.array([[1, 2, 3, 4, 5, 6],
                 [6, 7, 8, 9, 10,11]])
print(ary1)
print(ary1.shape)#(2, 6)表示2行6列 获取二维数组的行列数
print('1--------------')
# list二维
test_2D = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
zero_test_2D=np.zeros_like(test_2D)
ones_test_2D=np.ones_like(test_2D)
print(zero_test_2D)
print(ones_test_2D)
test_3D = [[[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]],
           [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
           ]
print('2--------------')
# ctrl+Alt+L 代码自动对齐
print(ary * 10)
print(ary + ary)
# np.arange 给定范围
a = np.arange(0, 5, 1)  # [0 1 2 3 4] (起始值，终止值，步长)
b = a + [1, 2, 3, 4, 5]  # np的列表类型和传统的列表是可以结合的
print(a, b)

# 创建zero数组
a1 = np.zeros(10)
print(a1)

a2 = np.ones(10,dtype='float32')
print(a2)
a3=np.ones(10)
print(a3)
print('3--------------')

#修改数组的纬度
ary=np.array([1,2,3,4,5,6])
print('数组的shape是',ary.shape)
ary.shape=(2,3)
print('经过shape变化后的数组是:')
print(ary)
ary.shape=(6,)
print(ary)

#元素数据的类型
print(ary.dtype)#int32  

