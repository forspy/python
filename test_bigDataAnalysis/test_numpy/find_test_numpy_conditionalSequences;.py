import numpy as np
a=np.array([1,2,3,4,5,6,7],dtype='float32')
#数组处理函数
conditionalA=np.piecewise(
    a,
    [a>4],
    [np.nan]
)
print(conditionalA)
print(a>4)#[False False False False  True  True  True]利用掩码进行位置标记
a[a>4]=np.nan#相当于matlab里面的find函数,可以根据掩码定位元素
print(a)
print(~np.isnan(a))#
import matplotlib.pyplot as mp
x=np.array([1,2,3,4,5,6,7])
mp.scatter(x,a)
mp.show()

