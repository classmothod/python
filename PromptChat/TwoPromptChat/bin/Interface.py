import time
# Função de exibir MSG + nome de usuário
def Interface(MSG):
    MeSG = ''
    Name = ''
    cont = 0
    for i in MSG: # salva primeira variável MeSG
        if i == '+': break
        else:
            MeSG = MeSG + i
            cont += 1 # Contador para Name
    Name = MSG[cont+1:]
    Day = time.ctime()
    Day = Day[11:19]
    # Exibe Menssage formatada.
    print('{}({}):'.format(Name,Day),MeSG)
    #print('                   ','{}─>'.format(Name),MeSG)
