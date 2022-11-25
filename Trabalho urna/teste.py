tabela1 = {'Arroz': 130,
                 'Feijão': 100,
                 'Batata': 80,
                 'Carne': 200,
                 'Frango': 150,
                 'Peixe': 100}
tabela2 = {'Ovo': 70,
                'Leite': 50,
                'Queijo': 100,
                'Iogurte': 60}
tabela3 = {'Abacaxi': 50,
            'Maçã': 40,
            'Banana': 80,
            'Pera': 60,
                            'Uva': 60}
comida1 = []
comida2 = []
comida3 = []
valor = 0
while valor < 140:
    for k, v in tabela1.items():
        valor += v
        comida1.append(k)
    print(comida1)
        