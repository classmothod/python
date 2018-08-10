#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "bin")
from Imports import *

if __name__ == '__main__':
    Welcome_() # Exibe Mensagem
    Parameters = Parameters() # Devolve Nome de Host
    porta = Porta() # Define Porta
    Name_Second = Name_User() # Nome de usuário
    tell = Send_MSG() # Atalho para Classe SenD_MSG

    tthread = tThread(Listening, newSocket(), tell, Parameters, porta)#Parameters = Host
    tthread.start() # Inica Thread

    WelcomeTwo(Parameters, porta) # Exibe Mensagem de Aguardo!
    print('')

    # Loop de Envio
    MSG = input()
    MSG = '\n' + MSG
    while True:
        tell.Envia(MSG, Name_Second) # Envia Mensagem
        MSG = input() # Nova mensagem para enviar

    tthread.join() # Fecha Thread
    newSocket.close() # Fecha conexão TCP
    exit() # EXIT()
