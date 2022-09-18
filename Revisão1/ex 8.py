""" 
Questão 8
Escreva um programa que calcula o desconto previdenciário de um funcionário. Dado um salário, o programa deve retornar o valor do desconto 
proporcional ao mesmo. O cálculo segue a regra: o desconto é de 11% do valor do salário, entretanto, o valor máximo de desconto é 334,29, 
o que for menor.

A resposta deve estar no seguinte formato: O desconto é de R$ X, onde X é o valor do desconto. Arredondar a média para 2 casas decimais. 
Para isso, use o formato %.2f.

    print(f'O desconto é de R$ {desconto:.2f}')
"""
salario = float(input("Informe seu salário "))
desconto = salario * 0.11
if desconto > 334.29:
    desconto = 334.29
print(f"O desconto é de R$ {desconto:.2f}, onde {desconto:.2f} é o valor do desconto.")