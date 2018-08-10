from Imports import *

def tThread(Listening, sock_tcp, tell, Host, porta): # Recebe parametros
    tthread = Thread(target=Listening, args=(sock_tcp, tell, Host, porta))
    return tthread # Retorna Thread criado!
