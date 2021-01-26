import aleatorio as a
import media as m

lista = a.geraListaInteiro(10)
print("minha lista: ",lista)

media = m.media(lista)
print("a media da minha lista e ", str(media))

mediana = m.mediana(lista)
print("a mediana da minha lista e ", str(mediana))

moda = m.moda(lista)
print("A Moda da minha lista e", str(moda))