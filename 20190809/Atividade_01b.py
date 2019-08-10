'''
1. Implemente um programa em Python que leia 15 números informados pelo usuário. Utilizando uma estrutura de pilha, realize as seguintes tarefas:
    a) Se o número for impar, adicione na pilha.
    b) Se o número for par, remova um elemento da pilha caso a pilha não seja vazia.

Ao final das 15 execuções, mostre a sequencia de operações realizadas e a pilha final.
'''

pilha1 = []  # Todos os itens
pilha2 = []  # Somente os Impares
x = 0
y = 0


def verifica_par():
    if(y % 2 != 0):
        pilha2.append(y)
    else:
        vazia()


def vazia():
    if(len(pilha2) == 0):
        print('Pilha vazia, digite um número Impar: ')
    else:
        pilha2.pop()


def lista():
    print('Pilha total: ', pilha1)
    print('Pilha Impar: ', pilha2)


while(x < 15):
    y = int(input('Digite um número: '))
    pilha1.append(y)
    verifica_par()
    x += 1


lista()
