from Imports import *

def newSocket(): # Cria Socket
    sock_tcp = socket(AF_INET, SOCK_STREAM)
    return sock_tcp # Retorna Socket
