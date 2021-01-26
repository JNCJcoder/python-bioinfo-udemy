# -*- coding: utf-8 -*-

import os

os.system("echo hello world")

os.system("pwd")

comando = input("deseja limpar a tela? ")
if comando == "s":
    os.system("clear")

os.system("python script2.py")


variavel = os.system("python script2.py > output.txt")

arquivo = open("output.txt").read()

print("mensagem do output: ", arquivo)


# Metodo Call

import subprocess

print("parte 1")
variavel = subprocess.call(["python","script2.py"])

print("parte 2")
print(variavel)


# Metodo Check_output

print("parte 1")
variavel = subprocess.check_output(["python","script2.py"])

print("parte 2")
print(variavel)


# 