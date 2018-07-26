import socket

PORT = 12345
server = socket.socket()

try:
	# empty string means server can connect to connections from other PC
	server.bind(('', PORT))
	print(f'socket binded to {PORT}')
except Exception as e:
	raise e

try:
	# 5 connections are made waiting
	server.listen(5)
	print('socket is listening')
except Exception as e:
	print(e)

# start accepting connections and closing them
while True:
	c, addr = server.accept()
	print(f"Connection from {addr}")
	c.send(b'Thanks for connecting')
	c.close()

# we connect at port and let it running
# open terminal and enter telnet localhost 12345 and you'll see the output
# run the socket_client_connection.py and you will see the results in terminal