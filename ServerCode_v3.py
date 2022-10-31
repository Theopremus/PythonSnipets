from socket import *
import sys

# Made some changes to the skeleton. Hope you don't mind.


def handle_request(server):
    connectionSocket, addr = server.accept()
    try:
        message = connectionSocket.recv(1000).decode("utf-8")
        filename = message.split()[1]
        f = open(filename[1:], mode='rb')
        filebin = f.read()
        header = "HTTP/1.1 200 OK\r\nContent-Length: {}\r\nContent-Type: image/jpeg\r\n\r\n".format(
            len(filebin))
        data = filebin + "\r\n".encode()
        connectionSocket.send(header.encode())
        connectionSocket.sendall(data)
        connectionSocket.close()
    except IOError:
        header = "HTTP/1.1 404 Not Found\r\n"
        print('File not Found')
        connectionSocket.send(header.encode())
        connectionSocket.close()


serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(("127.0.0.1", 5678))
serverSocket.listen()
while True:
    print('Ready to serve...')
    handle_request(serverSocket)
serverSocket.shutdown(SHUT_RDWR)
serverSocket.close()

sys.exit()  # Terminate the program after sending the corresponding data
