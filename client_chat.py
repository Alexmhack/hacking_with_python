import socket
import thread

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

BUFFSIZ = 1024
ADDR = (HOST, PORT)
client_socket.connect(ADDR)

HOST = input('ENTER HOST: ')
PORT = input('ENTER PORT: ')

if not PORT:
	PORT = 33000
else:
	PORT = int(PORT)

msg = input('ENTER MESSAGE: ')

while True:
	client_socket.send(bytes(msg, 'utf-8'))


def receive():
	while True:
		try:
			msg = client_socket.recv(BUFFSIZ)
			print(msg.decode('utf-8'))
		except OSError:
			break


receive_thread = thread.Thread(target=receive)
receive_thread.start()
receive_thread.mainloop()