import socket
import re

PATH_ERROR = "#@#".encode()
EXIT_MESSAGE = "#$#".encode()
SUCCESS_MESSAGE = "#!#"

client_socket = socket.socket()

# defining port and host
host = "localhost"
port = 12345

# Connect socket to the host and port
client_socket.connect((host, port))
print("Connection established...")

folder_path = input("Enter folder path in which files will be recieved: ")
if not folder_path[len(folder_path) - 1] == "\\":
    folder_path = folder_path + "\\"

while True:
    # send a request to the server
    while True:
        file_path = input("Enter path of the file to be received: ")
        if mathches := re.search(r".*\\(.*)$", file_path, re.IGNORECASE):
            receive_here = folder_path + mathches.group(1)
            client_socket.send(file_path.encode())
            break
        else:
            print("Invalid path!")

    data = client_socket.recv(1024)
    message = data.decode()
    if message == "#~#":
        print("[Server]: The specified file path does not exist!")
        client_socket.send(PATH_ERROR)
        continue

    try:
        # Write File in binary
        with open(receive_here, "wb") as file:
            message = ""
            while message != SUCCESS_MESSAGE:
                file.write(data)
                data = client_socket.recv(1024)
                message = data.decode()
        print("File has been received successfully.")
    except:
        print("Invalid folder path for receiving file!")
        client_socket.send(PATH_ERROR)

        folder_path = input("Enter folder path in which files will be recieved: ")
        if not folder_path[len(folder_path) - 1] == "\\":
            folder_path = folder_path + "\\"

        continue

    choice = input(
        "Enter 'exit' to end connection or 'continue' to continue receiving files: "
    )
    if choice == "exit":
        break

client_socket.send(EXIT_MESSAGE)
client_socket.close()
print("Connection closed.")
