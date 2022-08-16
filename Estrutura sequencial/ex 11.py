"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""

n1 = int(input("Numero 1 "))
n2 = int(input("Numero 2 "))
n3 = int(input("Numero 3 "))

r1 = (n1 * n1) * (n2/2)
print(r1)
r2 = (n1 * n1 * n1) + n3
print(r2)
r3 = n3 * n3 * n3
print(r3)