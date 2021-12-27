#solução 01:
'''dia, mes, ano = input("Digite sua data de nascimento no formato DD/MM/AAAA: ").split("/")

if mes == "01":
    mesNome = "Janeiro"
elif mes == "02":
    mesNome = "Fevereiro"
elif mes == "03":
    mesNome = "Março"
elif mes == "04":
    mesNome = "Abril"
elif mes == "05":
    mesNome = "Maio"
elif mes == "06":
    mesNome = "Junho"
elif mes == "07":
    mesNome = "Julho"
elif mes == "08":
    mesNome = "Agosto"
elif mes == "09":
    mesNome = "Setembro"
elif mes == "10":
    mesNome = "Outubro"
elif mes == "11":
    mesNome = "Novembro"
elif mes == "12":
    mesNome = "Dezembro"

print(f"Você nasceu em {dia} de {mesNome} de {ano}")'''

#soluçao 02: (com tratamento de excessões)
dia, mes, ano = input("Digite sua data de nascimento no formato DD/MM/AAAA: ").split("/")

meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]

try:
    mesInt = int(mes) - 1
except ValueError:
    print(f"Mês incorreto: {mes}")

else:
    print(f"Você nasceu em {dia} de {meses[mesInt]} de {ano}")


#SOLUÇÃO 01:

import locale
from data_e_hora import datetime as date
locale.setlocale(locale.LC_TIME, "pt_BR")

#obtem a data de nascimento
dtnascimento = input("Digite sua data de nascimento no formato dd/mm/aaaa: ")

#converte a strig para datetime
hoje = date.strptime(dtnascimento,"%d/%m/%Y")

#monta o texto desejado
texto = hoje.strftime("Você nasceu %d de mes de %Y")

#converte a primeira letra do Mes para maiuscula e realiza a substituicao da palavra mes na string acima
print(texto.replace('mes',hoje.strftime("%B").capitalize()))

#SOLUÇÃO 02:

#funcao para conversao o numero do mes para texto
def converteMesTexto(mes):
    mes = int(mes)
    if mes == 1:
        mesTexto = "Janeiro"
    elif mes == 2:
        mesTexto = "Fevereiro"
    elif mes == 3:
        mesTexto = "Março"
    elif mes == 4:
        mesTexto = "Abril"
    elif mes == 5:
        mesTexto = "Maio"
    elif mes == 6:
        mesTexto = "Junho"
    elif mes == 7:
        mesTexto = "Julho"
    elif mes == 8:
        mesTexto = "Agosto"
    elif mes == 9:
        mesTexto = "Setembro"
    elif mes == 10:
        mesTexto = "Outubro"
    elif mes == 11:
        mesTexto = "Novembro"
    elif mes == 12:
        mesTexto = "Fevereiro"
    else:
        mesTexto = "Erro"

    return mesTexto

#obtem a data de nascimento
dia, mes, ano = input("Digite sua data de nascimento no formato dd/mm/aaaa: ").split("/")

print(f"Você nasceu em {dia} de {converteMesTexto(mes)} de {ano}")
