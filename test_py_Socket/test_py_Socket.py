# 使用python来编写以各种方式使用网络程序
# python进行网络编程的好处
# 1.python提供了强大的网络编程支持，有很多库实现了常见的网络协议以及基于这些协议的抽象层，让你能够专注于程序的逻辑，而无需关心通过线路来传输byte的问题
# 2.python擅长处理字符解析


# socket模块
# socket是网络编程的基本组件
# socket是一个通信通道，两端各有一个程序srver/client端
# python的socket实例化的时候接收三个参数：1.地址族(默认socket.AF_INET)2.流套接字(默认socket.SOCK_STREAM)3.数据报套接字(默认socket.SOCK_DGRAM)，协议(默认0，IPV4协议)
# 服务器socket：
# 1.创建
# 2.初始化地址
# 3.绑定bind
# 4.监听listen(listen接收一个最长连接等待队列，超过这个队列就不进入等待连接队列直接拒绝)
# 5.accept阻塞(同步)等待直到接受客户端的连接，然后返回一个格式为(client,address)的元组，client是客户端的socket创建返回句柄
# 注：阻塞类似于windows消息事件循环里面的GetMessage 非阻塞类似于PeekMessage
# 客户端socket：
# 1.创建socket
# 2.connect服务器bind的地址(使用socket.gethostname获取当前机器的主机名) 地址是格式为(host,port)的元组 host为例如www.baidu.com（ip地址也可） port为端口

# 传输数据：
# 使用send和recv(需要指定最多依次接受多少个数据)

# 注意：linux系统中需要有管理员权限才能使用1024以下的端口号，这些端口较小的是提供给标准服务用的，比如80端口供给Web服务器使用
#可使用ctrl+c来停止服务器


