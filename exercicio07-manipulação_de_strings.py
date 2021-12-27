nome = input("Digite o nome: ")

for i in range(len(nome)+1):
    print(nome[:i].upper())

  #SOLUÇAÕ 01:

nome = input("Digite o nome: ").upper()

parte = ""

#para cada letra no nome
for letra in nome:
    #concatena na string parte
    parte += letra
    #imprime a string
    print(parte)

    #Solução 02

nome = input("Digite o nome: ").upper()

    # gera uma lista de numeros com o maior numero igual ao tamanho da string
for i in range(len(nome) + 1):
    # faz fatiamento sempre da posicao zero com o numero do for
    print(nome[0:i])

#SOLUÇÃO 03:

nome = input("Digite o nome: ").upper()

parte = ""

#para cada letra no nome
for i in range(len(nome)):
    #concatena na string parte
    parte += nome[i]
    #imprime a string
    print(parte)

