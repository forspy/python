import numpy as np
import matplotlib.pyplot as mp

mp.figure('pie')
values = [26, 17, 21, 29, 11]#占比
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]#扇形之间的间距
labels=['python','JavaScript','C++','Java','PHP']
colors=['dodgerblue','orangered','limegreen','violet','gold']
mp.pie(values,spaces,labels,colors,'%.2f%%',shadow=True,startangle=0,radius=1)
mp.axis('equal')#圆形

lst = np.array([1, 3,np.nan,4, 5])

print(np.sum(lst>=1),np.sum(~np.isnan(lst)),len(lst),np.shape(lst))#np中指定条件的长度，非Nan的个数，序列长度,维度


mp.show()
