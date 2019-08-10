'''
1. Implemente um programa em Python que leia 15 números informados pelo usuário. Utilizando uma estrutura de pilha, realize as seguintes tarefas:
    a) Se o número for impar, adicione na pilha.
    b) Se o número for par, remova um elemento da pilha caso a pilha não seja vazia.
    Ao final das 15 execuções, mostre a sequencia de operações realizadas e a pilha final.'''

pilha1 = []
pilha2 = []

x = 0
while (x < 15):
    y = int(input('Digite: '))
    pilha1.append(y)
    if ((y % 2) != 0):
        pilha2.append(y)
    else:
        if (len(pilha2) == 0):
            print('A Pilha está vazia, digite um número Impar: ')
            y = int(input('Digite: '))
        else:
            pilha2.pop()
    x += 1

print('Pilha Par: ',pilha1)
print('Pilha Impar: ',pilha2)
