list1=[[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],]

for row in range(0,3):
    line = []
    print(list1[row])#可以直接打印一行
    for column in range(0,4):
        line.append(list1[row][column])#也可以使用这种方式打印一行
    #print(line)
        #print(list1[row][column])

for row in range(0,3):
    for column in range(0,4):
        print(list1[row][column],end=' ') #在一行后面接上空格继续打
    print()

#对于不知道长度的矩阵,这个可以对于任意的二维纬度
def print_list(list):
    for row in range(len(list)):
        for column in range(len(list[row])):
            print(list[row][column],end=' ')
        print()#相当于回车

print_list(list1)