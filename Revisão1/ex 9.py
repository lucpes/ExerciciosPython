""" 
Questão 9
A série de Fibonacci é formada pela sequencia:

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Escreva um programa que gere a série de FIBONACCI até o N-ésimo termo (com N sendo uma entrada do algoritmo).

Deve ser impresso um número por linha.
"""
termo = 1
ultimo = 1
penultimo = 0
x = 1
while x <= 100:
    print(f"{x}-{termo}")
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    x += 1 
    