import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
puerto = 456
print(host)

serversocket.bind((host, puerto))
serversocket.listen(3)

while True:
    # Inicia la conexión
    clientsocket, address = serversocket.accept()
    print(type(address))

    # address es una tupla de dos valores
    print(1, '---', address[0]) # dirección IP
    print(1, '---', address[1]) # Número de conexión

    print("Recibo la conexión desde: " + str(address[0]))
    # Mensaje enviado
    mensaje = b'Hola Bienvenido a nuestro servidor' + b'\r\n'
    clientsocket.send(mensaje)
    clientsocket.close()