from Imports import *

# Classe principal!
class Send_MSG:
    def __init__(self):
        self.MSG_ = '' # Instacia Mensagem
        self.status = True # Retorna true para def loop_true
        self.Checks = None # Vai receber socket tcp / sock_tcp

    # Vai enviar mensagem...
    def Envia(self, MSG, Name_Second):
        self.MSG_ = MSG + '+' + Name_Second # Recebe a message
        if self.Checks != None:
            # Codifica MSG...
            self.Checks.send(str.encode(self.MSG_))
    # Retorn True para loop...
    def Looping(self):
        return self.status # Retorna True
