import socket

server_socket = socket.socket()

# defining port and host
host = 'localhost'
port = 12345

# binding to the host and port
server_socket.bind((host, port))

# accept up to 10 connections
server_socket.listen(10)
print('Server is listening...')

while True:
    # establish connection with the clients.
    connection, address = server_socket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))

    # Get data from the client
    req = connection.recv(1024)
    filepath = req.decode()
    print("[Client]: Requested file path:", filepath)

    try:
        # Read File in binary
        with open(filepath, 'rb') as file:
            line = file.read(1024)
            # Keep sending data to the client
            while(line):
                connection.send(line)
                line = file.read(1024)
        print('[Server] File has been transferred successfully.')
    except:
        message = "error_unique".encode()
        connection.send(message)

    connection.close()