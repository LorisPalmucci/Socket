import socket

def create_file(rcvData):
    with open('/Users/palm/Desktop/rcv_File.txt', 'a') as file:
        d = str(rcvData)
        file.write(d)

def createSocket():
    print('Create connection...')
    HOST = ''
    PORT = 50007
    mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('OK')
    print('Start Server...')
    mySock.bind((HOST, PORT))
    mySock.listen(2)
    print('Server is listen on:', PORT)
    acceptConnection(mySock)

def acceptConnection(socket):
        while True:
            conn, addr = socket.accept()
            print('Connect...')
            receiveData(conn, addr)
            print('Wait for data...')

def receiveData(conn, addr):
        with conn:
            print('Connected by', addr)
            while True:
                print('Receiving data...')
                data = conn.recv(1024)
                create_file(data)
                if not data: 
                    break
                print('Transfer COMPLETE')


if __name__ == "__main__":
    createSocket()


