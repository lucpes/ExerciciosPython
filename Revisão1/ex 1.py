"""
Questão 1
Ler três valores do teclado e dizer se eles formam um triângulo.

Caso afirmativo, dizer seu tipo (Equilátero, Isósceles ou Escaleno). Caso negativo, dizer Não é um triângulo.
"""
a = int(input("Informe o primeiro lado do triangulo "))
b = int(input("Informe o segundo lado do triangulo "))
c = int(input("Informe o terceiro lado do triangulo "))

if a + b > c and a + c > b and b + c > a:
    print("É um triangulo")
    if a == b and a == c:
        print("Equilátero")
    elif a == b or a == c:
        print("Isosceles")
    else:
        print("Escaleno")
else:
    print("Não é um triangulo ")