def Host():
    print(' ┌Endereço IP do outro usuário──♥')
    host = input(' └──> ')
    print('')
    while host == '':
        host = input(' └──> ')
    return host # Retorna Host

def Porta():
    print(' ┌Porta──♥')
    porta = input(' └──> ')
    print('')
    if porta == '':
        porta = 5621
    return int(porta)
