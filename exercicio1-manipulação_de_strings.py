#soluçao 01:
'''texto = input("Digite o texto a ser cifrado: ").upper()

#string com a sequencia do alfabeto iniciando em A
origem = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#string com a sequencia do alfabeto iniciando em D, pois queremos
#um deslocamente de 3 caracteres em relacao a string de origem
destino = "DEFGHIJKLMNOPQRSTUVWXYZABC"

#utilizamos o maketrans para gerar um mapa entre a primeira letra da string origem com a primeira letra da string destino
#a segunda letra da string origem com a segunda letra da string destino e assim sucessivamente.
translation = texto.maketrans(origem, destino)

#utilizamos o translate para realizar a substituicação conforme o mapa criado
print("Texo cifrado:", texto.translate(translation))'''

#soluçao 02:
'''texto = input("Digite o texto a ser cifrado: ").upper()
textocifrado = ""

# acessamos letra por letra do texto a ser cifrado
for letra in texto:
    # para cada letra verificamos se ela e apenas maiusculas e
    # minusculas, pois os demais caracteres na cifra de cesar nao sao cifrados
    if letra.isalpha():
        # if (decimal >= 65 and decimal <= 90):
        # se for caractere do tipo alpha, converte o caractere para o codigo decimal da tabela ascii
        # e soma mais 3 para realizar o deslocamento para o codigo da terceira letra da frente
        decimal = (ord(letra) + 3)

        # caso a soma resulte em um caractere fora do intervalo alpha
        if decimal > 90:
            # forcamos o codigo do caractere retornar para o inicio da lista permitida (codigos de 65 à 90)
            decimal = (decimal - 90) + 64

            # concatena a letra criptografada
        textocifrado += chr(decimal)
    else:
        # se o caractere nao for alpha nao faz nenhuma criptografia
        # simplesmente concatena junto com os demais caracteres
        textocifrado += letra

print(textocifrado)'''

#soluçao 03:
'''texto = "a ligeira raposa marrom saltou 3 vezes sobre o cachorro cansado que estrava entre ()".upper()
textocifrado = ""
#Utilizaremos uma string do alfabeto com suas respectivas posicoes dentro da lista para realizar a substituicao
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCD"

for letra in texto:
    localizacao = alfabeto.find(letra)
    if localizacao >= 0:
        novaLocalizacao = localizacao + 3
        if novaLocalizacao > 26:
            #realiza o enquadramento do caractere criptografado no inicio da lista
            #uma vez que so temos 26 caracteres
            novaLocalizacao = novaLocalizacao % 26
        #novaLocalizacao = localizacao + 3
        textocifrado += alfabeto[novaLocalizacao]
    else:
        textocifrado += letra

print(textocifrado)'''
