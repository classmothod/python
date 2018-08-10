#!/usr/bin/python3.6
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, "bin")
from Imports import *

if __name__ == '__main__':
    WelcomeOne_() # Exibe Mensagem
    Parameters = Host() # Devolve Nome de Host
    porta = Porta() # Define porta
    Name_Second = Name_User() # Nome de usuário
    tell = Send_MSG() # Atalho para Classe Send_MSG

    tthread = tThread(Listening, newSocket(), tell, Parameters, porta)
    tthread.start() # Inica Thread

    #WelcomeTwo_(Parameters) # Exibe Mensagem de Aguardo!

    # Loop de Envio
    MSG = input()
    while True:
        tell.Envia(MSG, Name_Second) # Envia Mensagem
        MSG = input() # Nova mensagem para enviar

    tthread.join() # Fecha Thread
    newSocket.close() # Fecha conexão TCP
    exit() # EXIT()
