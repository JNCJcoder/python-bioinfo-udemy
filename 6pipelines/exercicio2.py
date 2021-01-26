# -*- coding: utf-8 -*-

import os
import requests

sequencia = "P52407.fasta"
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
            cadeia = id_maior[5]

print("O PDB template é: ", id_maior,"(identidade = ", identidade, "% )")

url = "https://files.rcsb.org/download/" + id_maior + ".pdb"

r = requests.get(url)

w = open(id_maior+".pdb", "w")

w.write(">p1;"+id_maior+"\n")

comeco = None
fim = None


from Bio.PDB import *

pdb = open(id_maior+".pdb").readlines()
for linha in pdb:
    if linha[0:4] == "ATOM" and linha[21] == cadeia and linha[13:15] == "CA":
        resname3 = linha[17:20]

        if int(linha[22:26]) < comeco:
            comeco = int(linha[22:26])

        if int(linha[22:26]) > fim:
            fim = int(linha[22:26])

        resname1 = Polypeptide.three_to_one(resname3)
        w.write(resname1)

w.write("\n")
w.close()

os.system("cat "+id_maior+".fasta > alinha.fasta")
os.system("cat "+sequencia+" >> alinha.fasta")

os.system("clustalw -infile='alinha.fasta' -output='pir'")

aln = open("alinha.pir").readlines()
new_aln = open("new_alinha.pir", "w")

tipo = 0

seq = open(sequencia)
seq_final = ""
for linha in seq:
    if linha[0] != ">":
        seq_final += linha.strip()

tamanho_seq = len(seq_final)
print("tamanho da seq = ", str(tamanho_seq))

for linha in aln:
    if linha[0] == ">":
        if tipo == 0 and linha != "\n":
            new_aln.write(">P1;"+id_maior+"\n")
            new_aln.write("structure:"+id_maior+":"+str(comeco)+":"+str(fim)+":"+cadeia)
            tipo = tipo + 1
        if tipo == 1:
            new_aln.write(">P1;sequence\n")
            new_aln.write("sequence:"+sequencia+":"+str(1)+":A:"+str(tamanho_seq)+":A::::")
    else:
        new_aln.write(linha)

new_aln.close()