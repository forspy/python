# 在socket模块的基础上python自带了更加专业的SocketServer模块
# 模块SocketServer是标准库提供的服务器框架的基石，这个框架里包括BaseHTTPServer、SimpleHTTPServer、CGIHTTPServer、SimpleXMLRPCServer和DocXMLRPCServer
# 模块SocketServer包含4个最基本的服务器TCPServer（流式套接字）、UDPServer（数据报套接字）


# 使用SocketServer编写服务器的时候，大部分代码都位于请求处理器中，每当服务器收到客户端的连接请求时，都将实例化一个请求程序，并对其调用各种方法来处理请求
# 基本请求处理程序BaseRequestHandler将所有的操作都摆放在一个方法中--服务器调用的方法handle。这个方法可通过属性self.request来访问客户端的套接字

# 如果处理的是流式的套接字，可使用StreamRequestHandler类的方法，self.rfile(读取)，self.wfile(写入)
# 模块SocketServer还包含很多其他的类，它们为HTTP服务器提供基本的支持(如运行CGI脚本)，以及XML-RPC支持

from socketserver import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):  # 继承基类特性
    def handle(self):  # 服务器方法
        addr = self.request.getpeername()
        print('got connection from', addr)
        self.wfile.write('thank you for connecting'.encode())  # 写入文件等待发送


sever = TCPServer(('forspy', 1234), Handler)  # 1.forspy表示运行该服务器的计算机2.Handler表示回调函数，用于发送服务器写入的函数
sever.serve_forever()
