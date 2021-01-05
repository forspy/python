import numpy as np
#就地变维
a=np.arange(1,9)
print(a)
a.shape=(2,4)
print(a)
a.resize(2,2,2)#就地变维
print(a)
print("--------------")
#共享传递变维
b1=np.arange(1,9)
b2=b1.reshape(2,4)
print(b1)
print(b2)
b2[0,0]=999
b3=b2.ravel()#变为1维
print(b1,b3)
print('-------------')
#复制变维
c1=np.arange(1,10)
c2=c1.flatten()
c2[0]=999
print(c1,c2)

