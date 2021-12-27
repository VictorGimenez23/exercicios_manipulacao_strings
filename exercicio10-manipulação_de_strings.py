espacos = 16 * " "
print(f"Nome  {espacos}",end="")
print("Prova1   )

exit()
qtdeAlunos = int(input("Digite a quantidade alunos a ser lidos: "))

nomes = []
provas1 = []
provas2 = []
trabalhos1 = []
trabalhos2 = []
mediaFinal = []
status = []

for i in range(qtdeAlunos):
    nome = input("Digite o nome do aluno: ")
    trabalho1 = float(input("Digite a nota do trabalho 1: "))
    prova1 = float(input("Digite a nota da prova 1: "))
    trabalho2 = float(input("Digite a nota do trabalho 2: "))
    prova2 = float(input("Digite a nota da prova 2: "))

    nomes.append(nome)
    provas1.append(prova1)
    provas2.append(prova2)
    trabalhos1.append(trabalho1)
    trabalhos2.append(trabalho2)

    resultado = ((((trabalho1 +trabalho2 )/2)*3) + (((prova1 + prova2)/2)*7))/10
    mediaFinal.append(resultado)