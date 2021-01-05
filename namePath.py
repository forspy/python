import os
name1='1'
name2='2'
filename = os.path.join("riverFlux_{:}_{:}.dat".format(name1,name2))
print(filename)
addstr='world'
str='hello{:}'.format(addstr)
print(str)