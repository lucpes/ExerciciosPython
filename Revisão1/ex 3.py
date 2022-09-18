"""
Questão 3
Informe se um dado ano é ou não bissexto. Obs: um ano é bissexto se ele for divisível por 400 ou se ele for divisível por 4 e não por 100.

A resposta deve estar no seguinte formato: É bissexto ou Não é bissexto.
"""
ano = int(input("Informe o ano "))

if (ano%400) == 0:
    print("O ano é bissexto")
elif (ano%4) == 0 and (ano%100) != 0:
    print("O ano é bissexto")
else:
    print("O ano não é bissexto")