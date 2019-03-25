# 使用poll的简单服务器
# 调用poll时，将返回一个轮询对象，可以使用方法register向这个对象注册文件描述符(可使用unregister删除文件描述符)(文件描述符指的是fopen打开文件返回的int类型的文件标号)
# 注册对象后，可调用其方法poll，这将返回一个包含(fd,event)元组的列表，fd为文件描述符，event为发生的事件(位掩码)
# 比如POLLIN事件为文件描述符中有需要读取的数据
# 可以使用这样的方式来检查事件是否发生 if event&select.POLLIN:

import socket,select

s=socket.socket()
host=socket.gethostname()
port =1234
s.bind((host,port))
fdmap={s.fileno():s}

s.listen(5)
p=select.poll()#windows的select没有poll属性
p.register(s)
while True:
    events=p.poll()
    for fd,event in events:
        if fd in fdmap:
            c,addr=s.accept()
            print('got connection from',addr)
            p.register(c)
            fdmap[c.fileno()]=c
        elif event & select.POLLIN:
            data=fdmap[fd].recv(1024)
            if not data:
                print(fdmap[fd].getpeername(),'disconnected')
                p.unregister(fd)
                del fdmap
            else:
                print(data)