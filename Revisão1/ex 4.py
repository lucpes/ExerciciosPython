"""
Questão 4
Ler um número inteiro e dizer se ele é ou não um número primo.

A resposta deve estar no seguinte formato: É primo ou Não é primo.
"""
valor = 1
divisores = 0

n = int(input("Informe o número "))

if n > 0:
    while valor <= n:
        if (n%valor) == 0:
            divisores += 1
        valor += 1
        
    if divisores == 2:
        print(f"O número {n} é primo")
        
    else:
        print(f"O número {n} não é primo")
else:
    print("O valor não pode ser menor que zero")
