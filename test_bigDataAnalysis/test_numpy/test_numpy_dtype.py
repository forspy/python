# 对于一个三维数组，按照页行列来访问
# ary[0][1][2] 表示ary数组的第1页第2行第3列
import numpy as np

ary = np.array([[1, 2, 3, 4, 5, 6],
                [6, 7, 8, 9, 10, 11]])
# 遍历np数组
aryShape = ary.shape
print(aryShape)
# 逐个输出
for i in range(aryShape[0]):
    for j in range(aryShape[1]):
        print(ary[i][j])

# 按行输出
for i in range(aryShape[0]):
    print(ary[i])


#Numpy里面储存的类型
#布尔型bool
#有符号整数型int8(-128~127)/int16/int32/int64
#无符号整数型uint8(0~255)/uint16/uint32/uint64
#浮点型float16/float32/float64
#复数型complex64/complex128
#字符串型 一个Unicode字符占32位 =4字节  （8位1字节（byte））
#转化ary的数据类型

#缩写
# 类型	字符代码
# bool	?, b1
# int8	b, i1
# uint8	B, u1
# int16	h, i2
# uint16	H, u2
# int32	i, i4
# uint32	I, u4
# int64	q, i8
# uint64	Q, u8
# float16	f2, e
# float32	f4, f
# float64	f8, d
# complex64	F4, F
# complex128	F8, D
# str	a, S（可以在S后面添加数字，表示字符串长度，比如S3表示长度为三的字符串，不写则为最大长度）
# unicode	U
# object	O
# void	V
print(ary.dtype)
floatAry=ary.astype('float32')
strAry=ary.astype('str')
print(ary.dtype,floatAry.dtype,strAry)

#若数组中的数据类型不一样,可以考虑使用元组
data=[
    ('xiaoming',[1,2,3],15),
    ('xiaohong',[4,5,6],12),
    ('xiaowang',[7,8,9],13),
]

print(data)
#通过dtype设置数据类型
ary1=np.array(data,dtype='U8,3int32,int32')#需要说明数据类型，以便开辟内存空间U8表示使用8个Unicode字符（注：一个Unicode字符占4个字节）
print(ary1)
#通过字典设置数据类型
ary2=np.array(data,dtype={'names':['name','number','age'],'formats':['U8','3int32','int32']})
print(ary2[0]['number'])#以字典的形式查找输出
#
print(ary1,ary1.dtype)#"<"表示小端字节序

#日期识别 np.datetime64数据类型
testDate=['2011','2011-01-01','2011-01-02 08:00:01','2011-02']
testDates=np.array(testDate)
testDatesDay=testDates.astype('M8[D]')#精确到天
print(testDatesDay,testDatesDay.dtype)#能够自动识别日期并补全
testDatesHour=testDates.astype('M8[h]')#精确到小时
print(testDatesHour,testDatesHour.dtype)
testDatesSeconds=testDates.astype('M8[s]')#精确到秒
print(testDatesSeconds,testDatesSeconds.dtype)
#相差多少时间
print('相差多少时间:',testDatesHour[2]-testDatesHour[1])