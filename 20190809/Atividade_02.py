'''
2. Escreva um programa em Python que simule o controle de uma pista de decolagem de aviões em um aeroporto. Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas:
    a) Listar o número de aviões aguardando na fila de decolagem;
    b) Autorizar a decolagem do primeiro avião da fila;
    c) Adicionar um avião à fila de espera;
    d) Listar todos os aviões na fila de espera.'''

avioes = ['aviao1', 'aviao2']
count = 1
aviao = 'aviao'


def listar_avioes():
    print('Quantidade de avioes no aeroport', len(avioes))


def autorizar_decolagem():
    avioes.pop(0)
    print('autorizar decolagem')


def adicionar_aviao_a_fila():
    print()
    avioes.append('aviao_novo')
    print('adicionar aviao à fila')


def listar_avioes_da_fila():
    print(avioes)


def menu():
    print('\n')
    print('-------------------------------------------------------------')
    print('1 - Listar o número de aviões aguardando na fila de decolagem')
    print('2 - Autorizar a decolagem do primeiro avião da fila')
    print('3 - Adicionar um avião à fila de espera')
    print('4 - Listar todos os aviões na fila de espera')
    print('-------------------------------------------------------------')
    n = int(input('Escolha uma das opções: '))
    print(n)
    return n


def acoes():
    while 1 == 1:
        result = menu()
        if result == 1:
            listar_avioes()
        elif result == 2:
            autorizar_decolagem()
        elif result == 3:
            adicionar_aviao_a_fila()
        elif result == 4:
            listar_avioes_da_fila()
        else:
            print('Opção inválida')

acoes()
