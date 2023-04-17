import socket
from _thread import *
from time import sleep

PATH_ERROR = "#~#".encode()
EXIT_MESSAGE = "#$#"
SUCCESS_MESSAGE = "#!#".encode()


def handle_new_client(connection, address):
    print("Connected to: " + address[0] + ":" + str(address[1]))

    try:
        while True:
            # Get data from the client
            req = connection.recv(1024)
            request = req.decode()

            if request == "#@#":
                continue
            elif request == EXIT_MESSAGE:
                break

            print("[Client]: Requested file path:", request)

            try:
                # Read File in binary
                with open(request, "rb") as file:
                    data = file.read(1024)
                    # send data to the client
                    while data:
                        connection.send(data)
                        data = file.read(1024)
                sleep(0.1)
                connection.send(SUCCESS_MESSAGE)
                print("File has been transferred successfully.")
            except:
                connection.send(PATH_ERROR)

        print(address[0] + ":" + str(address[1]) + " is disconnected...")
        connection.close()
    except:
        print(address[0] + ":" + str(address[1]) + " is disconnected...")
        connection.close()


server_socket = socket.socket()

# defining port and host
host = "localhost"
port = 12345

# binding to the host and port
server_socket.bind((host, port))

# accept up to 10 connections
server_socket.listen(10)
print("Server is listening...")

while True:
    # establish connection with the clients.
    connection, address = server_socket.accept()
    start_new_thread(handle_new_client, (connection, address))
