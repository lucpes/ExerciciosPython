"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
 Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
  Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.

"""

salario_h = float(input("Quanto voce ganha por hora? "))
horas = float(input("Quantas horas voce trabalha em um mes? "))

salario_b = salario_h * horas
desconto_ir = salario_b * 0.11
desconto_i = salario_b * 0.08
desconto_s = salario_b * 0.05
salario_l = salario_b - desconto_i - desconto_s

print(f"+ Salário Bruto : R$ {salario_b}")
print(f"- Imposto de Renda (11%) : R$ {desconto_ir}")
print(f"- INSS (8%) : R$ {desconto_i}")
print(f"- Sindicato (5%) : R$ {desconto_s}")
print(f"= Salário Liquido : R$ {salario_l}")