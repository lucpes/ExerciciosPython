"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""

f = float(input("Qual a temperatura em Fahrenheit? "))
c = 5 * ((f-32)/9)
print(c)

c = float(input("Qual a temperatura em Celsius? "))
f = ((c*9)/5)+32
print(f)