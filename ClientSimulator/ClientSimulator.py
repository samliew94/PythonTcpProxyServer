# Echo client program
import socket

print("Client Startup")
HOST = 'localhost'    # The remote host
PORT = 3333          # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while(True):

        msg = input("Client -> ").encode()
        s.sendall(msg)
        data = s.recv(1024)
        print('Server <- ', repr(data))
        print()
