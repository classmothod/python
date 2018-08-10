from Imports import *

def Listening(sock_tcp, tell, host, porta):
    Origem = (host, porta)
    sock_tcp.bind(Origem)# Se conecta paralelamento
    sock_tcp.listen(1) # Escuta um cliente!

    while True:# True... pela class def
        Checks, User=sock_tcp.accept()
        User = User[0]
        WelcomeUser(User)
        # Send_MSG.Checks = socket(AF_INET, SOCK_STREAM)
        tell.Checks=Checks

        while True: # True...
            MSG = Checks.recv(1024) # Recebe MSG
            if not MSG: break
            MSG = str(MSG,'utf-8')
            Interface(MSG) # Envia mensagem para outra Função
