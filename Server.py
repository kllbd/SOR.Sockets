import socketserver
import hashlib


class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(4096).strip()
        md5 = hashlib.md5()
        md5.update(self.data)
        hashnumber = md5.hexdigest()
        print("[{}] {} escreveu: {}".format(hashnumber, self.client_address[0], self.data.decode('ascii')))
        # print(self.data.decode('ascii'))
        self.request.sendall("{} ({})".format(self.data.decode("ascii").upper(), hashnumber).encode())


class Main:
    HOST, PORT = "localhost", 9999
    ENDPOINT = (HOST, PORT)
    server = socketserver.TCPServer(ENDPOINT, MyTCPHandler)
    print("Servidor rodando.")
    server.serve_forever()
