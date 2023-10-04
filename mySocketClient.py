import socket
from fileRead.myjson import readJson
import json
import sys

def createSocket():
    print('Create connection...')
    HOST = input('HOST: ')
    PORT = int(input('port: '))
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('OK')
    print('Connect to: ',HOST, PORT)
    connect(client, HOST, PORT)
    return client

def connect(socket, host, port):
    socket.connect((host,port))
    print('connesso a: ',host, port)

def sendFile(sock):
    data = json.dumps(readJson(), indent=4)
    if (data == 'null'):
        exit()
    dataBytes = bytes(data.encode('utf-8'))
    print('Send file...')
    sock.sendall(dataBytes)
    print('COMPLETE')

if __name__ == "__main__":
    c = createSocket()
    sendFile(c)