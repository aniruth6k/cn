# server.py
import socket

s = socket.socket()
print("Socket successfully created")

port = 12345
s.bind(('', port))
print("Socket binded to %s" % port)

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting'.encode())
    c.close()
    break  # Note: This will exit after one connection
    
# client.py
import socket

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
print(s.recv(1024).decode())
s.close()
