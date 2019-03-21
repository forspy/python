#客户端
import socket
s=socket.socket()

host=socket.gethostname()
port=1234

s.connect((host,port))
while True:
    arr = s.recv(1024)
    if arr:
        print(arr)