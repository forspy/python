import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as mdates

#日期的格式化读入
def func(ymd):
    ymd=str(ymd,encoding='utf-8')#bytes转成字符串must be str, not bytes
    time=dt.datetime.strptime(ymd,'%Y/%m/%d')#将str类型转化为time数据类型,time为datetime类
    #print('------------',time)
    t=time.date().strftime('%Y-%m-%d')#将datetime类型转化为str
    #t=t[0::]
    return t

#func('2011/1/1')
#np的文件读取
data=np.loadtxt(
    './appleData.csv',#文件路径
    delimiter=',',#分隔符 科使用notepad++查看
    usecols=(0,1,3,4),#读取哪些列
    unpack=False,#是否按列拆包,True表示返回多个一维数组（可以是使用多个变量去接），False表示返回一个二维数组
    dtype='U6,M8[D],int32,float32',#数据类型M8[D]是时间类型，D表示精确到天
    converters={1:func},#转换器函数字典，第1列回调func函数进行日期的转化将2011/1/1转化为2011-1-1
)

print(data.dtype)
print(data)
print('-----------')
print(data[0])
print('============')
#也可以按列返回多个一维数组
AAPL_TIME,data1,data2=np.loadtxt(
    './appleData.csv',  # 文件路径
    delimiter=',',  # 分隔符 科使用notepad++查看
    usecols=(1, 3, 4),  # 读取哪些列
    unpack=True,  # 是否按列拆包,True表示返回3个一维数组，False表示返回一个二维数组
    dtype='M8[D],int32,float32',  # 数据类型
    converters={1: func},  # 转换器函数字典，第1列回调func函数进行日期的转化将2011/1/1转化为2011-1-1
)
#AAPL_TIME=AAPL_TIME.astype('M8[M]')
print(AAPL_TIME,AAPL_TIME.dtype)#可以作为横轴，AAPL_TIME是一个datetime64类型的数据
#如果觉得年太长，可以只写月日
#AAPL_TIME=AAPL_TIME.astype('M8[M]')
#AAPL_TIME=AAPL_TIME
#绘制射线图
#-----设置中文
mp.rcParams['font.sans-serif'] = ['SimHei']  # chinese SimHei
mp.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

mp.figure('AAPL')
mp.title('折线图')
#如果x轴识别的不好就将np.ndarray的数据类型转化为matplotlib.dates的数据类型更加保险
#AAPL_TIME=AAPL_TIME.astype(mdates.datetime.datetime)
mp.scatter(AAPL_TIME,data1,label='时间序列点')
#=========
mp.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))#设置X轴坐标格式，去除年份
#每周一个主刻度
#mp.gca().xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=mdates.MO))#每周一个主刻度

#=========

mp.xlabel('时间',fontsize=10)
mp.ylabel('值',fontsize=10)

mp.plot(AAPL_TIME,data1,label='时间折线图')


#绘制平均线
mean=np.mean(data1)
mp.hlines(mean,AAPL_TIME[0],AAPL_TIME[-1],colors='orangered',label='均线')

#mp.gcf().autofmt_xdate()  # 自动旋转日期标记

#返回序列的最大值/最小值
mp.scatter(AAPL_TIME[np.argmax(data1)],np.max(data1),c='red')
#显示最大值
mp.text(AAPL_TIME[np.argmax(data1)],np.max(data1),np.max(data1),va='bottom')

mp.scatter(AAPL_TIME[np.argmin(data1)],np.min(data1),c='blue')
#显示最小值
mp.text(AAPL_TIME[np.argmin(data1)],np.min(data1),np.min(data1),va='top')
#显示中位数线
median=np.median(data1)
mp.hlines(median,AAPL_TIME[0],AAPL_TIME[-1],colors='black',label='中位数线')
#标准差：表征样本的离散程度
#sqrt((q1^2+q2^2+...+qn^2)/(n-1))#q表示离差（离平均值）
stddata=np.std(data1)
mp.hlines(stddata,AAPL_TIME[0],AAPL_TIME[-1],colors='green',label='标准差线')

mp.grid()
mp.legend(loc=0)
#按行按列进行轴向汇总
#1.先将data1和data2垂向进行上下拼接
horizontaldata=np.vstack((data1,data2)).transpose()
print(horizontaldata)
#2.写好回调函数
def stackfunc(arraydata):
    return arraydata.mean()

#进行轴向汇总
meandata=np.apply_along_axis(stackfunc,1,horizontaldata)#1表示按照水平方向传入数组
print(meandata)
mp.show()
#加权平均算法
#s=(a1*w1+a2*w2+...+an*wn)/(a1+a2+...+an) a表示权重 w表示值



