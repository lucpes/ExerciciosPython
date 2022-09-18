"""
    Exemplo
Escreva um programa que leia três números e mostre o maior entre eles.

A resposta deve estar no seguinte formato: O maior número é X, onde X é o maior número lido.
"""
maior = 0
n1 = int(input("Escreva o primeiro número "))
n2 = int(input("Escreva o segundo número "))
n3 = int(input("Escreva o terceiro número "))

if n1 > maior:
    maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print(f"O maior número é {maior}")