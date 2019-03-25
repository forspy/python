# 分叉服务器
from socketserver import TCPServer, ForkingMixIn, StreamRequestHandler


class Server(ForkingMixIn, TCPServer): pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('got connection from', addr)
        self.wfile.write('thank you for connecting')


server = Server(('', 1234), Handler)
server.serve_forever()

#注意windows不支持线程分叉fork