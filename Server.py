import socketserver
import hashlib


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(4096).strip()
        md5 = hashlib.md5()
        md5.update(self.data)
        hashnumber = md5.hexdigest()
        print("{} escreveu: {} ({})".format(self.client_address[0], self.data.decode('ascii'), hashnumber))
        # print(self.data.decode('ascii'))
        self.request.send("{} ({})".format(self.data.decode("ascii"), hashnumber).encode())


class Main:
    HOST, PORT = "localhost", 9999
    ENDPOINT = (HOST, PORT)
    server = socketserver.TCPServer(ENDPOINT, MyTCPHandler)
    print("Servidor rodando.")
    server.serve_forever()