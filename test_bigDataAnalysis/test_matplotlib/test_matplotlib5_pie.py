import numpy as np
import matplotlib.pyplot as mp

mp.figure('pie')
values = [26, 17, 21, 29, 11]#占比
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]#扇形之间的间距
labels=['python','JavaScript','C++','Java','PHP']
colors=['dodgerblue','orangered','limegreen','violet','gold']
mp.pie(values,spaces,labels,colors,'%.2f%%',shadow=True,startangle=0,radius=1)
mp.axis('equal')#圆形
mp.show()
