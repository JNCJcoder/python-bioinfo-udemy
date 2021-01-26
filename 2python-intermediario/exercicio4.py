
menu = 0

def abrirArquivo():
    nome = input("Digite o nome do arquivo: ")

    arquivo = open(nome)

    return arquivo

def lerArquivo(arquivo):
    linhas = arquivo.readlines()

    for linha in linhas:
        print(linha.strip())
    

while menu != 3:
    print("(1) Abrir Arquivo\n(2) Ler Arquivo aberto\n(3) Sair\n")

    menu = int(input("Digite a opcao desejada: "))

    if menu == 1:
        arquivo = abrirArquivo()
    elif menu == 2:
        lerArquivo(arquivo)
