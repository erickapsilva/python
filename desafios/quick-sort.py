'''
Created on 4 de mai de 2017

@author: erickapsilva


Disciplina: 06283 - Laboratório de Programação BSI 

Implemente o algoritmo quicksort em python 3.x.

Entrada: o programa deverá ler uma única string com input() 
contendo vários inteiros separados por um espaço
Saída: o programa deverá imprimir os inteiros em ordem crescente 
usando print() separados por um espaço. Não há espaço nem ENTER após o último elemento.

ENTRADA:
5 3

SAÍDA:
3 5
'''


entrada = input()
entradaQuebrada = entrada.split(" ") 
listaInteiros = []
for e in entradaQuebrada:
    listaInteiros.append(int(e))

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    menor, igual, maior = [],[],[]
    pivo = lista[0]
    for l in lista:
        if l < pivo:
            menor.append(l)
        elif l == pivo:
            igual.append(l)
        else:
            maior.append(l)
    return quicksort(menor) + igual + quicksort(maior)

retorno = quicksort(listaInteiros)

resposta = " ".join(str(r) for r in retorno)

print(resposta)








