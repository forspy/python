# Twisted时一个事件驱动的python网络框架
# 支持Web服务器和客户端，SSH2、SMTP、POP3、IMAP4、AIM、ICQ、IRC、MSN、Jabber、NNTP、DNS
# https://www.lfd.uci.edu/~gohlke/pythonlibs/  下载地址
# (python -m pip install --upgrade pip 先在cmd下升级pip  可考虑)
# 注意尽量在cmd下面进行安装，因为权限足

# pip install Twisted-18.9.0-cp37-cp37m-win_amd64.whl
from twisted.internet import reactor  # 执行Twisted里面的reactor框架

from twisted.internet.protocol import Protocol, Factory


class SimpleLogger(Protocol):
    def connectionMade(self):
        print('got connection from', self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, 'disconnected')

    def dataReceived(self, data):
        print(data.decode())


factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()

# 总结：socket--基本网络通信通道
# urllib/urllib2 能够从服务器张读取和下载数据
# 框架 SocketServer 包含一系列服务器基类  还支持简单CUI的web服务器 如果要处理多个客户端请求，必须使用分叉或线程化
# select/poll 能够在一组连接中找出为读取和写入准备就绪的链接，这样就能以循环的方式为多个链接提供服务，从而营造出能够处理多个链接的假象--异步I/O
# Twisted--异步框架，支持大多数网络协议
