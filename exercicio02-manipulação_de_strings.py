def substituir(frase,palavra):
    variavel = frase.split()
    ultimaPalavra = variavel[-1]
    return frase.replace(ultimaPalavra,palavra)

frase = input("Frase: ")
palavraNova = input("Palavra: ")

fraseNova = substituir(frase, palavraNova)

print(fraseNova)