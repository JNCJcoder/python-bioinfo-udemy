sequencia = input("Digite uma sequencia: ")

arquivo = open("seq.fasta", "w")

arquivo.write(">seq\n")
arquivo.write(sequencia)

arquivo.close()