# 线程化服务器
from socketserver import TCPServer, ThreadingMixIn, StreamRequestHandler


class Server(ThreadingMixIn, TCPServer): pass


class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('got connection from', addr)
        self.wfile.write('thank you for connecting'.encode())  # 文本在计算机和网络中传输的大小端差异


server = Server(('', 1234), Handler)
server.serve_forever()
