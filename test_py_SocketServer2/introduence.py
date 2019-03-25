# 当有多个客户端连接请求时，需要能够同时处理多个连接
# 主要方法有三种：分叉(forking)、线程化和异步I/O
# 缺点：
# 1. fork是一种轻量化的进程复制，需要占用资源较多，而且客户端很多时可能出现伸缩性不佳，取决于CPU的数量(fork进程可以理解为平行宇宙)

# 2.线程化可能会带来同步和互斥的问题

# 在分叉服务器中，对于每一个客户端连接，都将通过分叉创建一个子进程，父进程继续监听新连接，而子进程负责处理客户端的请求，客户端请求结束后，子进程直接退出
# 使用类似于线程的并行方式，名为微线程，其伸缩性比真正的线程高的多
# 线程共享进程的资源，减少了资源的占用

# 异步I/O的基本机制时模块select中的函数select----Twisted是一个非常强大的异步网络编程框架


