""" 
Questão 6
Solicitar a idade de uma pessoa em anos, meses e dias e informar na tela a idade em dias. Considere sempre um ano com 365 dias e um mês com 30 dias.

Caso o usuário digite uma idade inválida (negativa ou com meses > 12 ou com dias > 30), deve ser impressa a mensagem Idade inválida e ler a idade novamente.

A resposta deve estar no seguinte formato: A idade em dias é X, onde X é a idade em dias.
"""

while True:
    ano = int(input("Informe sua idade em anos "))
    if ano < 0 or ano > 120:
        print("Idade inválida")
    else:
        break
while True:
    meses = int(input("Informe os meses "))
    if meses < 0 or meses >= 12:
        print("Idade inválida")
    else:
        break
while True:
    dias = int(input("Informe os dias "))
    if dias < 0 or dias >= 30:
        print("Idade inválida")
    else:
        break
ano = ano*365
meses = meses*30
resultado = ano + meses + dias

print(f"Sua idade, em dias, é {resultado} dias")