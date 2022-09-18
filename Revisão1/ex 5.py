""" 
Questão 5
Faça um algoritmo que leia as 3 notas de um aluno e calcule a média final deste aluno.

Apenas aceite valores entre 0 e 10.0. Caso o usuário digite um valor fora deste intervalo, deve ser impressa a mensagem Nota Inválida
e ler a nota novamente.

Considerar que a média é ponderada e que o peso das notas é: 2,3 e 5, respectivamente.

A resposta deve estar no seguinte formato: A média final do aluno é X, onde X é a média final do aluno. Arredondar a média para 2 
casas decimais. Para isso, use o formato %.2f.

    print(f'A média final do aluno é {media:.2f}')
"""
"""n1 = -1
while n1 < 0 or n1 > 10:
    n1 = int(input("Primeira nota do aluno "))"""

while True:
    n1 = float(input("Primeira nota do aluno "))
    if n1 < 0 or n1 > 10:
        print("Nota inválida")
    else:
        break
while True:
    n2 = float(input("Segunda nota do aluno "))
    if n2 < 0 or n2 > 10:
        print("Nota inválida")
    else:
        break
while True:
    n3 = float(input("Terceira nota do aluno "))
    if n3 < 0 or n3 > 10:
        print("Nota inválida")
    else:
        break
n1 = n1*2
n2 = n2*3
n3 = n3*5
print(f"A média do aluno foi {(n1+n2+n3)/10:.2f}")