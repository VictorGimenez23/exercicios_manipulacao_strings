#A vira T e T vira A; C vira G e G vira C;

#solução 01:
'''filamento = input("Digite o filamento de DNA: ")
complemento = ""

for letra in filamento:
    if letra == "A":
        complemento = complemento + letra.replace("A","T")

    elif letra == "T":
        complemento = complemento + letra.replace("T","A")

    elif letra == "C":
        complemento = complemento + letra.replace("C","G")

    elif letra == "G":
        complemento = complemento + letra.replace("G","C")

print(complemento)'''

#solução 02:
filamento = input("Digite o filamento de DNA: ")


traducao = filamento.maketrans("ATCG","TAGC")
print(filamento.translate(traducao))
