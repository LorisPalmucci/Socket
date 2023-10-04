import socket
from fileRead.myjson import readJson
import json

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
    print('Send file...')
    data = json.dumps(readJson(), indent=4)
    dataBytes = bytes(data.encode('utf-8'))
    sock.sendall(dataBytes)
    print('COMPLETE')

if __name__ == "__main__":

    c = createSocket()
    sendFile(c)