import socket

host = "127.0.0.1"            # The server IP
port = 8080                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
  url = raw_input("Url: ")
  s.send(url)
#data = s.recv(1024)
#print('Received', repr(data))
