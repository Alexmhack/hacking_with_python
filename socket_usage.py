import sys
import socket

# a socket instance with two args
# AF_INET relates to address family IPV4
# SOCK_STREAM means connection oriented TCP protocol

try:
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print('socket successfully created')
except socket.error as e:
	print(e)

# default port for socket
port = 80

try:
	# resolved google ip
	host_ip = socket.gethostbyname('www.google.com')
except socket.gaierror as e:
	print(e)
	sys.exit

# connecting to google ip
server.connect((host_ip, port))
print(f'Socket connected successfully at {host_ip}')

# you can find the ip using > ping url
# or use python socket
ip = socket.gethostbyname('www.google.com')
print(ip)