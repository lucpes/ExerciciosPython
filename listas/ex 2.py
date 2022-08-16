"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor 
a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0."""

notasAlunos = []

for x in range(1, 3):
    notas = []
    print("")
    for y in range(1, 5):
        n = int(input(f"Digite a {y} nota do aluno "))
        notas.append(n)
    notasAlunos.append(notas)

acimaMedia = 0
for aluno in notasAlunos:
    if sum(aluno) / len(aluno) >= 7:
        acimaMedia += 1

print(acimaMedia)



    


