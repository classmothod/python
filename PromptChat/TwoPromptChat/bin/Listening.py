from Imports import *

def Listening(sock_tcp, tell, host, porta):
    Destino = (host, porta)
    sock_tcp.connect(Destino)# Se conecta paralelamento
    print("\n ┌Conectado com o usuário", Destino[0])
    print(" └──Dê um Olá \(^v^)/ \n")

    while tell.Looping():# True... pela class def
        tell.Checks=sock_tcp

        while tell.Looping(): # True...
            MSG = sock_tcp.recv(1024) # Recebe msg
            if not MSG: break
            MSG = str(MSG,'utf-8')
            Interface(MSG) # Envia Mensagem Para uma função
