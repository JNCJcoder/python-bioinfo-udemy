# -*- coding: utf-8 -*-

# Listas 1

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1, 2, 3, 4, 5]
minha_lista_3 = ["abacaxi", 2, 9.89, True]

tamanho = len(minha_lista)

print(tamanho)

minha_lista.append("limao")

print(minha_lista)

if 7 in minha_lista_2:
    print("7 esta na lista")

if 3 in minha_lista_2:
    print("3 esta na lista")

del minha_lista[2:]
print(minha_lista)

minha_lista_4 = []

minha_lista_4.append(57)

# Listas 2

lista = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]

lista.sort()

print(lista)

lista.sort(reverse=True)

lista = sorted(lista)

print(lista)

lista.reverse()

print(lista)

lista2 = ["bola", "abacate", "dinheiro"]

lista2.sort(reverse=True)

print(lista2)


# Dicionarios

meu_dicionario = {
    "A": "AMEIXA",
    "B": "BOLA",
    "C": "CACHORRO"
}

print(meu_dicionario["A"])
print(meu_dicionario)


for chave in meu_dicionario:
    print(chave, ":", meu_dicionario[chave])


for i in meu_dicionario.items():
    print(i)

for i in meu_dicionario.values():
    print(i)

for i in meu_dicionario.keys():
    print(i)



# Strings

a = "Jorge"
b = "Netto"

concatenar = a + " " + b

print(concatenar)

tamanho = len(concatenar)

print(tamanho)

print(a[2])

print(concatenar[0:4])




# Funçoes

def soma(a, b):
    print(a + b)

soma(2, 3)

def soma2(a, b):
    return a + b

s = soma2(2, 3)
print(s)

def multiplicar(a, b):
    return a * b

m = multiplicar(2, 3)
print(m)

print(soma(s, m))


# Arquivos

arquivo = open("arquivo.txt")

print(arquivo)

linhas = arquivo.readlines()

print(linhas)

for linha in linhas:
    print(linha)

texto_completo = arquivo.read()

print(texto_completo)



w = open("arquivo2.txt", "w")

w.write("Esse eh o meu arquivo")

w.close()

we = open("arquivo2.txt", "a")

we.write("Esse eh o meu arquivo")

we.close()


# excessoes

a = 2
b = 0

try:
    print(a/b)
except:
    print("nao e permitido divisao por 0")


# Numeros Aleatorios

import random

random.seed(1)
numero = random.randint(0, 10)
print(numero)

lista = [6, 45, 9]
numero = random.choice(lista)

