# media, mediana, moda

# from statistics import *

# mean(lista)
# median(lista)
# mode(lista)

def media(lista):
    Media = sum(lista) / float(len(lista))
    return Media



def mediana(lista):
    lista_ordenada = sorted(lista)
    t = len(lista_ordenada)

    if t % 2 == 0:
        Mediana = (lista_ordenada[int(t / 2)] + lista_ordenada[int((t / 2) - 1)]) / 2
    else:
        Mediana = lista_ordenada[int(t / 2)]

    return Mediana

def moda(lista):
    lista_dic = {}

    for l in lista:
        if l not in lista_dic:
            lista_dic[l] = 1
        else:
            lista_dic[l] += 1
    
    maior_repeticao = max(lista_dic.values())

    for i in lista_dic:
        if lista_dic[i] == maior_repeticao:
            Moda = i
    
    return Moda