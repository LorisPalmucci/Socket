import socket
from fileRead.myjson import readJson
import json

HOST = '192.168.1.18'
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    print('Creazione connessione')
    client.connect((HOST,PORT))
    print('connesso a: ',HOST,':',PORT )
    data = json.dumps(readJson(), indent=4)
    #data.encode('utf-8')
    dataBytes = bytes(data.encode('utf-8'))
    #print(dataBytes)
    client.sendall(dataBytes)
    print('Connessione terminata')