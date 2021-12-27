# SOLUÇÃO 01:
# funcao para remover todos os espacos a esquerda de uma frase, a direita de uma frase e espacos
# duplicados entre as frases
def removeEspacos(frase):
    temp = ""
    # remove espacos a esquerda
    frase = frase.lstrip()

    # remove espacos a direita
    frase = frase.rstrip()

    # flag para detectar que a ja existe um espaco
    jaTemEspaco = False

    # para cada letra da frase
    for i in frase:
        # se a letra for igual a vazio e nao existir um espaco na etapa anterior do loop atual
        # entende que e o primeiro espaco e aceita a inclusao deste espaco
        if (i == " " and jaTemEspaco == False):
            # concatena os caracteres na string temporaria
            temp += i
            # coloca a flag no estado de que ja tem um espaco
            jaTemEspaco = True
        # se o caractere for diferente de espaco
        elif i != " ":
            # concatena o caractere
            # e muda o status da flag para nao tem espaco na etapa atual
            temp += i
            jaTemEspaco = False
            # como nao tem nenhum condicao para o caso de "é espaco e jaTemEspaco == True" nao faz nada
        # removendo todos os espacos apos o primeiro espaco existente depois de uma letra
    return temp


def numeroCaracteres(frase):
    frase = removeEspacos(frase)
    return len(frase)


def numeroPalavras(frase):
    frase = removeEspacos(frase)
    lista = frase.split(" ")
    return len(lista)


print(numeroCaracteres("    Rogerio     de Freitas "))
print(numeroPalavras("    Rogerio     de Freitas "))


# SOLUÇÃO 02:

def removeEspacos(frase):
    # transforma a string em uma lista
    fraseTemp = ""

    for item in frase.split():
        fraseTemp += item + " "

    return fraseTemp.strip()

def numeroCaracteres(frase):
    frase = removeEspacos(frase)
    return len(frase)

def numeroPalavras(frase):
    frase = removeEspacos(frase)
    lista = frase.split(" ")
    return len(lista)

print(numeroCaracteres("    Rogerio     de Freitas "))
print(numeroPalavras("    Rogerio     de Freitas "))
