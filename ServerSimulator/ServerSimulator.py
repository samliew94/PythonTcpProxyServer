# Echo server program
import socket

HOST = ''        # Symbolic name meaning all available interfaces
PORT = 10000              # Arbitrary non-privileged port
print('Starting up Server')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print("Server <-", data)
            if data:
                res = b'Sample Server Respond'
                print("Server -> ", res)
                conn.sendall(res)