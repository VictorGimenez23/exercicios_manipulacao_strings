texto = "Socorram-me, subi no onibus em Marrocos!"

textoLimpo = ""
for i in texto:
    if i.isalpha():
        textoLimpo += i

textoRev = textoLimpo[::-1]
comp = (textoRev.lower() == textoLimpo.lower())

print(comp)