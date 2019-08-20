import socket

host = 'localhost'        # All available interfaces
port = 8080               # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(str(host)+":"+str(port))
while True:
  s.listen(1)
  conn, addr = s.accept()
  print('Connected by', addr)
  while True:

    try:
      url_file = open("sent-info.txt", 'a')
      data = conn.recv(1024)
      if not data: break
      url_file.write(str(data)+'\n')
      url_file.close()

    except socket.error:
      print "Connection to client lost."
      break
  conn.close()
