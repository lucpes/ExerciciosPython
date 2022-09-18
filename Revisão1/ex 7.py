""" 
Questão 7
Construa um programa que receba um número e verifique se ele é um número triangular. (Um número é triangular quando é resultado
do produto de três números consecutivos. Exemplo: 24 = 2 x 3 x 4)

A resposta deve estar no seguinte formato: É triangular: {x} x {y} x {z}, sendo x, z e z os números que formam o número triangular,
ou Não é triangular.
"""
valor = 1
resultado = 0
x = int(input("Informe um número "))

if x > 0:
    while valor <= x:
        if (x%valor) == 0 and (x%(valor+1)) == 0 and (x%(valor+2)) == 0 and valor * (valor+1) * (valor+2) == x:
            print("O número é triangular")
            resultado += 1
            break
        else:
            valor += 1
    if resultado == 0:
        print ("O número não é triangular")

else:
    print("Informe um número maior que zero")