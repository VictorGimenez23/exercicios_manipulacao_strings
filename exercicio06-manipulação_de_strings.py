nome = input ("Digite o nome do usuário: ")

novonome = ""
for i in range(len(nome)-1,-1,-1):
    novonome += nome[i].upper()

print(novonome)

#SOLUÇÃO 01:
nome = input("Digite o nome: ").lower()

#utilizamos o fatiamento para inverter a string
print(nome[::-1])

#SOLUÇÃO 02:

nome = input("Digite o nome: ").lower()

reverso = ""

#acessamos individualmente cada posicao da string de forma inversa
for i in range(len(nome)-1,-1,-1):
    reverso += nome[i]

print(reverso)
