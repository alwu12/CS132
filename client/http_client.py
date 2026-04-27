import sys
from socket import *

def client_hard():
    serverName = 'localhost'
    serverPort = 6789

    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    fileName = input('Input file name to search')
    #fileName = input('')
    request = f"GET /{fileName} HTTP/1.1\r\nHost: {serverName}\r\n\r\n"
    clientSocket.send(request.encode())
    serverData = clientSocket.recv(1024)
    print(serverData.decode())
    clientSocket.close()


def main(serverName, serverPort, fileName):
    

    clientSocket = socket(AF_INET,SOCK_STREAM)
    clientSocket.connect((serverName,int(serverPort)))
    request = f"GET /{fileName} HTTP/1.1\r\nHost: {serverName}\r\n\r\n"
    clientSocket.send(request.encode())
    response = b""
    while True:
        data = clientSocket.recv(1024)
        if not data:
            break
        response += data

    print(response.decode(errors="ignore"))
    clientSocket.close()



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 http_client.py <serverName> <serverPort> <fileName>")
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])