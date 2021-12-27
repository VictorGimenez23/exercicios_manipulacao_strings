def func1():
    nome = "rogerio de freitas ribeiro"
    nometemp = list(nome)
    nometemp[0] = nometemp[0].upper()
    nome = ''
    for c in nometemp:
        nome += c
    # print(nome)


def func2():
    nome = "rogerio de freitas ribeiro"

    #nome = nome[0].upper + nome[1:]


def func3():
    nome = 'rogerio de freitas ribeiro'
    nome = nome.capitalize()
    # print(nome)


func1()
func2()
func3()

print(time.timeit("func1()", globals=globals(), number=500000))
print(time.timeit("func2()", globals=globals(), number=500000))
print(time.timeit("func3()", globals=globals(), number=500000))

#SOLUÇÃO 01:

#transforma o nome lido em uma lista quebrando as palavras por espaco
nome = input("Digite o seu nome: ").split()
nomeConvertido = ""
#para cada item da lista
for i in nome:
    #analisa se a quantidade de caracteres for menor ou igual a 3 converte a primeira letra para minusculo
    if len(i) <= 3:
        #concatena o item na string com tudo minusculo
        nomeConvertido += i.lower() + " "
        #caso contrario converte a primeira letra para maiusculo
    elif len(i) > 3:
        #concatena o item na string com a primeira em maiusculo
        nomeConvertido += i.title() + " "
#imprime o nome convertido
print(nomeConvertido)

#SOLUÇÃO 02:

#transforma todas as palavras do nome lido na primeira em maiusculo em uma lista quebrando as palavras por espaco
nome = input("Digite o seu nome: ").title().split()
nomeConvertido = ""
pedaco = ""
#para cada item da lista
for i in nome:
    #armazena o pedaco
    pedaco = i
    #se o tamanho do pedado for menor ou igual a 3
    if len(i) <= 3:
        #converte para minusculo e sobrescreve o valor em pedaco
        pedaco = i.lower()
    #concatena o pedaco em uma variavel do tipo string
    nomeConvertido += pedaco + " "

print(nomeConvertido)

#SOLUÇÃO 03:

nome = input("Digite o seu nome: ").title()
espacoAntes = 0
espacoDepois = 0

while True:
    #faz o espaco antes apontar para a posicao do espacodepois
    espacoAntes = espacoDepois
    #encontra o proximo espaco a partir da posicao do espacoAntes
    espacoDepois = nome.find(" ", espacoAntes + 1)

    #se algum dos espacos armazenarem -1 é porque nao foi encontrado espacos
    if (espacoAntes == -1 or espacoDepois == -1):
        #finaliza o laço
        break
    #caso contrario, conta quantos caracteres tem a subpalabra encontrada
    elif (((espacoDepois-1) - (espacoAntes+1)) <= 3):
        #obtem a subpalavra
        pedacoAntes = nome[espacoAntes+1:espacoDepois]
        #converte a subpalavra para minuscula
        pedacoDepois = pedacoAntes.lower()
        #realiza a substituicao da palavra antiga pela nova
        nome = nome.replace(pedacoAntes,pedacoDepois)

print(nome)