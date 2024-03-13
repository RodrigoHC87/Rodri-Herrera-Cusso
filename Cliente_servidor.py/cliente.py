import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.5.181'
puerto = 456
clientsocket.connect((host, puerto))

mensaje = clientsocket.recv(1024)
clientsocket.close()
print(mensaje.decode('ascii'))