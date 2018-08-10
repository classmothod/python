from Imports import *

def tThread(Listening, sock_tcp, tell, Parameters, porta): # Recebe parametros
    tthread = Thread(target=Listening, args=(sock_tcp, tell, Parameters, porta))
    return tthread # Retorna Thread criado!
