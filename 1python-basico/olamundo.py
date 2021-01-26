# -*- coding: utf-8 -*-

# Hello World

minha_variavel = "Olá, Mundo!"

print(minha_variavel)


# Variaveis

var1 = 1                    # Variavel Inteira
var2 = 1.1                  # Variavel Float
var3 = "Eu sou uma string"  # Variavel String
var4 = True                 # Variavel Booleano

print(var1)
print(var2)
print(var3)
print(var4)



# Operadores

x = 2
y = 3

soma = x + y

print(x == y)
print(soma < y)

# Operadores Logicos

x = 3
y = 3
z = 4

print(x == y or x == z and z == y)

# Estrutura Condicional

x = 1
y = 10000000

if x > y:
    print("x e maior que y")

if y > x:
    print("y e maior que x")


# elif

x = 1
y = 2

if x == y:
    print("numeros iguais")
elif y > x:
    print("y maior que x")
elif y > x:
     print("y maior que x")
else:
    print("numeros diferentes")


# Repetições

x = 1

while x < 10:
    print(x)
    x += 1


lista1 = [1,2,3,4,5]
lista2 = ["ola", "mundo", "!"]
lista3 = [0, "ola", "biscoito", 99.9, True]

for i in lista1:
    print(i)

for i in lista2:
    print(i)

for i in lista3:
    print(i)

for i in range(10, 20, 2):
    print(i)