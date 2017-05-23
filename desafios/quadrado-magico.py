'''
Created on 11 de mai de 2017

@author: erickapsilva

Aqui está o link do desafio: 
http://olimpiada.ic.unicamp.br/pratique/programacao/nivel2/2011f2p2_magico



'''
def somaDiagonalPrincipal(matriz,tam):
    somaPrin = 0
    for i in range(tam):
        somaPrin += matriz[i][i]
    return somaPrin

def somaDiagonalSecundaria(matriz,tam):
    somaSec = 0
    indice = tam -1
    for i in range(tam):
        somaSec += matriz[indice][indice]
        indice -=1
    return somaSec

def somarLinhas(matriz):
    somaLinhas = 0
    linhasIguais = False
    for m in matriz:
        soma = sum(m)
        if soma == sum(m):
            linhasIguais = True
            somaLinhas = soma
    if linhasIguais:
        return somaLinhas
    else:
        return 0


entrada = input()

entradaFormatada = entrada.split(" ")

arrayNumeros = []

for e in entradaFormatada:
  arrayNumeros.append(int(e))

tamanhoMatriz = arrayNumeros[0]

matriz = []
for i in range(tamanhoMatriz):
  matriz.append([0]*tamanhoMatriz)
indice = 1
for i in range(tamanhoMatriz):
  for j in range(tamanhoMatriz):
    matriz[i][j] = arrayNumeros[indice]
    indice+=1

dp = somaDiagonalPrincipal(matriz,tamanhoMatriz)
ds = somaDiagonalSecundaria(matriz,tamanhoMatriz)
s =  somarLinhas(matriz)

if dp == ds == s:
    print(s)
else:
    print("-1")
