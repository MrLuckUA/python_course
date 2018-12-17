import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 9999))
s.sendall('Hello, world'.encode('utf-8'))
data = s.recv(1024)
s.close()
print('Received', data.decode('utf-8'))
