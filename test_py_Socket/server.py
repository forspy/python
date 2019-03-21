# 一个简单的服务器
import socket

s = socket.socket()  # 实例化一个socket对象

host = socket.gethostname()  # connect服务器bind的地址(使用socket.gethostname获取当前机器的主机名) 地址是格式为(host,port)的元组 host为例如www.baidu.com（ip地址也可） port为端口

port = 1234
s.bind((host, port))
s.listen(5)  # 最大等待队列5个
c, addr = s.accept()
while True:
    #c, addr = s.accept()
    print('Got connection from', addr)
    arr=input('server:')
    c.send(arr.encode())
c.close()

#注意str通过encode()方法可以编码为指定的bytes，反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：