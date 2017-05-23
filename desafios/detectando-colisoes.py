'''
Created on 5 de mai de 2017

@author: erickapsilva

Aqui está o link do desafio: 
http://olimpiada.ic.unicamp.br/pratique/programacao/nivel1/2007f1p1_colisoes

*considero aqui que as entradas estão em uma linha só, de 4 em 4*

'''

entrada = input()
elementos = []

for n in entrada.split(" "):
    elementos.append(int(n))
    
    
if (elementos[2] < elementos[4]) or (elementos[6] < elementos[0]) or (elementos[3] < elementos[5]) or (elementos[7] < elementos[1]) or (elementos[0] > elementos[6]) or (elementos[4] > elementos[2]) or (elementos[1] > elementos[7]) or (elementos[5] > elementos[3]):
    print(0)
else:
    print(1)