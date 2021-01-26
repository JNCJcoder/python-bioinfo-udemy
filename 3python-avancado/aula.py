# List comprehension

x = [1, 2, 3, 4, 5]
y = []

for i in x:
    y.append(i**2)

print(x)
print(y)

x = [1, 2, 3, 4, 5]
y = [i**2 for i in x]
z = [i for i in x if i%2==1]

print("Usando list comprehension")
print(x)
print(y)
print(z)

# Enumerate

lista = ["abacate", "bola", "cachorro"]

for i in range(len(lista)):
    print(i, lista[i])


for i, nome in enumerate(lista):
    print(i, nome)


# Filter

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def pares(i):
    if i % 2 == 0:
        return i


lista_pares = filter(pares, lista)
print(list(lista_pares))

# Reduce

from functools import reduce

lista = [1, 3, 5, 10, 20]

def soma(x, y):
    return x * y

soma = reduce(soma, lista)
print(soma)


# Map

def dobro(x):
    return x * 2

valor = [1, 2, 3, 4, 5]

valor_dobrado = map(dobro, valor)

print(valor_dobrado)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)


# Lambda

valor_dobrado = map(lambda i: i*2, valor)

valor_dobrado = list(valor_dobrado)
print(valor_dobrado)


# Zips

lista1 = [1, 2, 3, 4, 5]
lista2 = ["acabate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["2,00", "5,00", "sem preco", "sem preco", "sem preco"]
for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)
