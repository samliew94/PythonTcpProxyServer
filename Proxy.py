import socket
from threading import Thread
import time

class Proxy2Server(Thread):
    
    def __init__(self, host, port):
        super(Proxy2Server, self).__init__()
        self.game = None # game client socket not known yet
        self.host = host
        self.port = port
        self.server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((host, port))

    def run(self):
        while True and self.server:
            data = self.server.recv(4096)
            if data:
                print("Server","<-",data)
                self.game.sendall(data)

class Game2Proxy(Thread):
    
    def __init__(self, host, port):
        super(Game2Proxy, self).__init__()
        self.server = None
        self.host = host
        self.port = port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((host, port))
        sock.listen(1)
        self.game, addr = sock.accept()

    def run(self):
        while True:
            data = self.game.recv(4096)
            if data: # forward to server                
                print('Client (ori) <- ', data)
                encoded = b'modified data'
                print('Server (edited) -> ', encoded)
                
                self.server.sendall(encoded)

class MyProxy(Thread):
    def __init__(self, fromHost, toHost):
        super(MyProxy, self).__init__()
        self.fromHost = fromHost
        self.toHost = toHost

    def run(self):
        while True:
            print("proxy setting up")
            self.g2p = Game2Proxy(self.fromHost, 3333) # G2P is using server code
            self.p2s = Proxy2Server(self.toHost, 10000) # P2S using client code
            print("proxy conn established")

            self.g2p.server = self.p2s.server
            self.p2s.game = self.g2p.game

            self.g2p.start()
            self.p2s.start()

masterServer = MyProxy('localhost', 'localhost')
masterServer.start()