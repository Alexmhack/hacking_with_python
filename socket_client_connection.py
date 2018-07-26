import socket

client = socket.socket()
PORT = 12345

client.connect(('127.0.0.1', PORT))

data = client.recv(1024)
print(data)
print(data.split())

client.close()