import os

menor = 99999999999
menor_id = ''

for _, _, arquivos in os.walk("/home/ryzen/Desktop"):
    for arquivo in arquivos:
        if arquivo[-4:] == ".pdb":
            
            linha = open(arquivo).readlines()
            
            try:
                score = linha[1]
                score = float(score[40:])

                if score < menor:
                    menor = score
                    menor_id = arquivo
            except:
                print("Modelo Invalido")

print("O melhor modelo é", menor_id)