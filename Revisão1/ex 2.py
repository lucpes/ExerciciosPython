"""
Questão 2
Ler 10 números inteiros e calcular a soma dos que forem par.

A resposta deve estar no seguinte formato: A soma dos números pares é X, onde X é a soma dos números pares lidos.
"""
resultado = 0
for x in range(1,11):
    x = int(input(f"Escreva o {x} número "))
    if (x%2) == 0:
        resultado = resultado + x

print(f"A soma dos números pares é {resultado}, onde {resultado} é a soma dos números pares lidos.")