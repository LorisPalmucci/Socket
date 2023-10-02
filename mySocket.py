import socket

HOST = ''
PORT = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mySock:
    print('Creazione connessione...')
    mySock.bind((HOST, PORT))
    mySock.listen(5)
    print('Server is listen on:', PORT)
    conn, addr = mySock.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data: break
            # conn.sendall(data)
        print('Connessione terminata dal client')
        #conn.close
