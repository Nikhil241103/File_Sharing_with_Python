import socket

sock = socket.socket()

# defining port and host
host = 'localhost'
port = 12345

# binding to the host and port
sock.bind((host, port))

# accept up to 10 connections
sock.listen(10)
print('Server is listening...')

while True:
    # establish connection with the clients.
    con, addr = sock.accept()
    print('Connected with ', addr)

    # Get data from the client
    req = con.recv(1024)
    filepath = req.decode()
    print("[Client]: Requested file path:", filepath)

    try:
        # Read File in binary
        with open(filepath, 'rb') as file:
            line = file.read(1024)
            # Keep sending data to the client
            while(line):
                con.send(line)
                line = file.read(1024)
        print('[Server] File has been transferred successfully.')
    except:
        message = "error_unique".encode()
        con.send(message)

    con.close()