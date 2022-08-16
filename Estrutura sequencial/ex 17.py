"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
 da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que
a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
arredonde os valores para cima, isto é, considere latas cheias.
"""

area = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))

litro = area/6
latas = litro/18
galao = litro/3.6

if latas == int(latas):
    print(f"Voce vai precisar de {int(latas)} lata(s)")
else:
    latas += 1
    print(f"Voce vai precisar de {int(latas)} lata(s)")

if galao == int(galao):
    print(f"Voce vai precisar de {int(galao)} galoes")
else:
    galao += 1
    print(f"Voce vai precisar de {int(galao)} galoes")


latas_1 = litro/latas
sobra = litro%latas
galao_r = sobra/galao

if galao_r == int(galao_r):
    print(galao_r)
else:
    galao_r += 1

print(f"Vão ser usadas {int(latas)} latas e {int(galao_r)} galoes")

"""litros = m2/6
latas = litros/18
galao = litros/3.6

restoLATA = litros % 18
restoGALÃO = restoLATA / 3.6
folga = restoGALÃO*10/100

print(restoLATA)
print(restoGALÃO)
print(folga)

if restoGALÃO > (int(restoGALÃO) + folga):
    print("A quantidade de latas é {} e a de galões é {}".format(int(latas), int(restoGALÃO)+1))
    print("O preço a se pagar é {} R$\n".format(int(latas)*80 + (int(restoGALÃO)+1)*25))
elif restoGALÃO < (int(restoGALÃO) + folga):
    print("A quantidade de latas é {} e a de galões é {}".format(int(latas), int(restoGALÃO)))
    print("O preço a se pagar é {} R$\n".format(int(latas)*80 + (int(restoGALÃO))*25))"""