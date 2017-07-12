#echo_client.py

import socket
import sys
from format import input_format

HOST = socket.gethostname()
PORT = 8080
ADDR = (HOST, PORT)
BUF_SIZE = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

if len(sys.argv) < 2 :
	print("No enough parameter")
	sys.exit(1)

data = input_format(sys.argv[1:])
print data

client.sendall(data)
res = client.recv(1024).split('\n')
client.close()

print('Retrive results:')
for line in res:
	print(line)