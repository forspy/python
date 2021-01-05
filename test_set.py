a=[1,1,2,2,3,7,6,6,5,8]

a1=set(a)
print(a1)

aa=[[1,'a'],[1,'a'],[2,'c'],[3,'d']]
print(aa)
#aa2=set(aa)
#思路，先转化为元组，再转化为序列,因为元组可哈希
#aa2=list(set([tuple(t) for t in aa]))
aa2=list(set(tuple(t) for t in aa))
list1=list(list(items) for items in aa2)
list1.sort()
print(list1)
#[(2, 'c'), (1, 'a'), (3, 'd')]
#[(3, 'd'), (1, 'a'), (2, 'c')]
#t1=()
#for t in aa:
#    print(tuple(t))
#aa2.sort()
#print(aa2)