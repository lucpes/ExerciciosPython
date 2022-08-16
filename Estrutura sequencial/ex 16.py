"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta
a serem compradas e o preço total.
"""

area = int(input("Qual o tamanho em metros quadrados da área a ser pintada? "))

litro = area/3
lata = int(litro/18)
preço = int(lata*80)

print(f"Vão ser necessárias {lata} latas de tinta a um preço de {preço} reais")

