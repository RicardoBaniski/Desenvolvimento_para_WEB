'''
2. Escreva um programa em Python que simule o controle de uma pista de decolagem de aviões em um aeroporto. Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas:
    a) Listar o número de aviões aguardando na fila de decolagem;
    b) Autorizar a decolagem do primeiro avião da fila;
    c) Adicionar um avião à fila de espera;
    d) Listar todos os aviões na fila de espera.'''

avioes = []
x = 0
a = 0


def adicionar():
    a = int(input('\nDigite o número do avião: '))
    avioes.append(a)


def lista_espera():
    if(len(avioes) == 0):
        print('\nNão há fila de espera')
    else:
        print('\nLista de espera: ', avioes)


def quantidade_espera():
    if (len(avioes) == 0):
        print('\nNão há fila de espera')
    else:
        print('\nAviões em espera: ', len(avioes))


def decolagem():
    if (len(avioes) == 0):
        print('\nNão há fila de espera')
    else:
        avioes.pop(0)


def menu():
    print('')
    print('Selecione uma opção:')
    print('1 - Quantidade de espera')
    print('2 - Autorizar decolagem')
    print('3 - Adicionar à espera')
    print('4 - Fila de espera')
    opc()


def opc():
    x = int(input('Opção: '))
    if(x == 1):
        quantidade_espera()
    elif (x == 2):
        decolagem()
    elif (x == 3):
        adicionar()
    elif (x == 4):
        lista_espera()
    menu()


menu()
