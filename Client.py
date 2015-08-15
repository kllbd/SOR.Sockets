import socket
import re


HOST, PORT = "localhost", 9999
ENDPOINT = (HOST, PORT)

repattern = '^(?P<message>(?=.*\d)(?=.*[a-z])\S{2,})$'


def getvalidmsg():
    userinput = input()
    while not re.match(repattern, userinput, re.I):
        print("Digite uma mensagem valida!")
        userinput = input()
    return userinput


def sendmsg(message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(ENDPOINT)
    except:
        return "Erro ao conectar ao servidor!"
    try:
        sock.sendall(message.encode('ascii'))
    except:
        return "Erro ao enviar a mensagem!"
    serverreturn = sock.recv(4096)
    sock.shutdown(0)
    sock.close()
    return serverreturn.decode('ascii')


while 1:
    print("Digite a mensagem: ")
    data = getvalidmsg()
    received = sendmsg(data)
    print("Enviado:  {}".format(data))
    print("Recebido: {}".format(received))
