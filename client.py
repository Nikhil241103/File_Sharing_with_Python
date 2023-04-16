import socket
import re

client_socket = socket.socket()

# defining port and host
host = 'localhost'
port = 12345

# Connect socket to the host and port
client_socket.connect((host, port))
print('Connection established...')

folder_path = input("Enter folder path in which files will be recieved: ")
if not folder_path[len(folder_path) - 1] == "\\":
    folder_path = folder_path + "\\"

while True:
    # send a request to the server
    while True:
        file_path = input("Enter path of file to be received: ")
        if mathches :=re.search(r".*\\(.*)$", file_path, re.IGNORECASE):
            folder_path = folder_path + mathches.group(1)
            client_socket.send(file_path.encode())
            break
        else:
            print("Invalid path!")

    line = client_socket.recv(1024)
    message = line.decode()
    if message == "error_unique":
        print("[Server]: The specified file path does not exist!")
        break

    try:
        # Write File in binary
        with open(folder_path, "wb") as file:
            while(line):
                file.write(line)
                line = client_socket.recv(1024)
        print('File has been received successfully.')
    except:
        print("Invalid path for receiving file!")

    client_socket.close()
    print('Connection Closed.')
    break