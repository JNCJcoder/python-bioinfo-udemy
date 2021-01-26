# -*- coding: utf-8 -*-

import os
import requests

os.system("blastp -query P52407.fasta -subject fasta.txt -outfmt=6 > resultado.txt")

resultado = open("resultado.txt").readlines()

maior = 0
identidade = ''
id_maior = ''

for linha in resultado:
    colunas = linha.split("\t")

    atual = float(colunas[11])
    identidade = float(colunas[2])

    if atual > maior:
        if identidade > 25:
            maior = atual
            id_maior = colunas[1]
            id_maior = id_maior[0:4]

print("O PDB template é: ", id_maior,"(identidade = ", identidade, "% )")

url = "https://files.rcsb.org/download/" + id_maior + ".pdb"

r = requests.get(url)

w = open(id_maior+".pdb", "w")

w.write(r.text)