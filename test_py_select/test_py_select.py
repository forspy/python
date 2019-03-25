#当服务器与客户端通信时，来自客户端的数据可能时断时续，如果使用了分叉和线程化：一个进程/线程等待数据的时候，其他进程/线程可继续处理客户端
#另一种做法是只处理当前正在通信的客户端，无需不断监听，只需要将监听后的客户端加入队列即可----框架asyncore/asynchat 和Twisted
#基于select函数或者poll函数(都位于select模块中)，其中放入poll可伸缩性更高，但只支持linux系统

#函数select包含三个必选参数和一个可选参数，前三个为序列，后一个为超时时间
import socket,select
s=socket.socket()

host=socket.gethostname()
port=1234
s.bind((host,port))
s.listen(5)#最大队列等待数
inputs=[s]#socket()返回句柄包装成序列
while True:
    rs,ws,es=select.select(inputs,[],[])#selcet返回三个序列即一个长度为3的元组，其中每个序列都包含有数据需要读取的所有输入文件描述符
    #例如第一个序列包含有数据需要读取的所有输入文件描述符
    for r in rs:
        if r is s:
            c,addr=s.accept()
            print('got connection from',addr)
            c.send('hello'.encode())
            inputs.append(c)
        else:
            try:
                data=r.recv(1024)
                disconnected=not data
            except socket.error:
                disconnected=True
            if disconnected:
                print(r.getpeername(),'disconnected')
                inputs.remove(r)
            else:
                print(data)