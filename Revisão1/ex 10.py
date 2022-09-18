""" 
Questão 10
O cardápio de uma lancheria é o seguinte:

Especificação	Código	Preço
Cachorro quente	100	1,20
Bauru simples	101	1,30
Bauru com ovo	102	1,50
Hambúrger	103	1,20
Cheeseburguer	104	1,30
Refrigerante	105	1,00
Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche. Considere que a 
cada execução somente será calculado um item.

Caso o código do item não seja válido, deve ser impressa a mensagem Código inválido e ler o código novamente. Caso a quantidade seja
inválida (menor ou igual a zero), deve ser impressa a mensagem Quantidade inválida e ler a quantidade novamente.

A resposta deve estar no seguinte formato: O valor a ser pago é R$ X, onde X é o valor total do pedido. Arredondar a média para 2 
casas decimais. Para isso, use o formato %.2f.

    print(f'O valor a ser pago é R$ {valor:.2f}')
"""
texto  = '''
Cardápio Lanchonete do seu ZÉ
Especificação   |Código  |  Preço
Cachorro Quente | 100    | R$ 1,20
Bauru Simples   | 101    | R$ 1,30
Bauru com ovo   | 102    | R$ 1,50
Hambúrguer      | 103    | R$ 1,20
Cheeseburguer   | 104    | R$ 1,30
Refrigerante    | 105    | R$ 1,00
'''

produtos = []
quantidades = []
precos = []

print(texto)

while True:
    print("")
    codigo = input("Digite o código do seu pedido: (exit) - para  sair do programa ")
    if codigo == 'exit':
        break

    if codigo == '100':
        qtde = int(input("Quantas unidades você vai querer de Cachorro quente? "))
        produtos.append('Cachorro quente')
        quantidades.append(qtde)
        precos.append(1.2*qtde)

    elif codigo == '101':
        qtde = int(input("Quantas unidades você vai querer de Bauru Simples? "))
        produtos.append('Bauru Simples')
        quantidades.append(qtde)
        precos.append(1.3*qtde)

    elif codigo == '102':
        qtde = int(input("Quantas unidades você vai querer de Bauru com ovo? "))
        produtos.append('Bauru com ovo')
        quantidades.append(qtde)
        precos.append(1.5*qtde)

    elif codigo == '103':
        qtde = int(input("Quantas unidades você vai querer de Hambúrguer? "))
        produtos.append('Hambúrguer')
        quantidades.append(qtde)
        precos.append(1.2*qtde)

    elif codigo == '104':
        qtde = int(input("Quantas unidades você vai querer de Cheeseburguer? "))
        produtos.append('Cheeseburguer')
        quantidades.append(qtde)
        precos.append(1.3*qtde)

    elif codigo == '105':
        qtde = int(input("Quantas unidades você vai querer de Refrigerante? "))
        produtos.append('Refrigerante')
        quantidades.append(qtde)
        precos.append(1.0*qtde)

    else:
        print("Item não encontrado, tente novamente.")
        continue

total = sum(precos)

print("")
for indice, i in enumerate(produtos):
    print(f"{i} x{quantidades[int(indice)]} = {precos[int(indice)]:.2f}")

print(f"Total: {total:.2f}")