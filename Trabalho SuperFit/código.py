while True:
    sexo = input('Informe seu sexo:(M ou F) ')
    sexo = sexo.lower()
    if sexo == 'm' or sexo == 'f':
        break
    else:
        print('Valor inválido')
idade = int(input('Informe sua idade: '))
altura = float(input('Informe sua altura:(em centímetros) '))
peso = float(input('Informe seu peso:(em kg) '))
while True:
    exercicio = input('Informe o nível de exercicio físico realizado:(leve, moderada ou intensa) ')
    if exercicio == 'leve':
        v_exercicio = 1.55
        break
    elif exercicio == 'moderada':
        v_exercicio = 1.84
        break
    elif exercicio == 'intensa':
        v_exercicio = 2.2
        break
    else:
        print('Valor inválido')
print()

'''print('Leve: fator médio de 1,55: considera atividades como cozinhar, cuidar de crianças; trabalhar 8 horas sentado e caminhadas de até 1 hora por dia;\n ')
print('Moderada: fator médio de 1,84: inclui atividades como fazer uma hora diária de exercícios como corrida, ciclismo, natação ou dança, trabalhar como operário de construção,  garçom, vendedor de porta em porta, carteiro o entregador de mercadorias leves;\n ')
print('Intensa: fator médio de 2,2: considera atividades como natação, corrida, andar de bicicleta ou dançar duas horas por dia; trabalhadores rurais não mecanizados (que trabalham com instrumentos manuais e caminham longas distâncias, várias horas por dia) ou entregador de objetos pesados.\n ')'''

alimentos = {}
calorias_total = []

while True:
    print('-'*6 + 'O que deseja?'+'-'*6)
    print('1 - Informar alimentos\n2 - Exibir o balanço energético\n3 - Solicitar uma nova dieta')
    r = input()
    if r == '1':
        alimento = input('Informe o alimento: ')
        alimento = alimento.lower()
        calorias = float(input('Quantas calorias esse alimento tem? '))
        alimentos[alimento] = calorias
        print()
    elif r == '2':
        for v in alimentos.values():
            calorias_total.append(v)
        calorias_total = sum(calorias_total)
        
        if idade >= 0 and idade <= 3:
            if sexo == 'm':
                e_basal = (59.512 * peso) - 30.4
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
            elif sexo == 'f':
                e_basal = (58.317 * peso) - 31.1
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
        elif idade > 3 and idade <= 10:
            if sexo == 'm':
                e_basal = (22.706 * peso) + 504.3
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
            elif sexo == 'f':
                e_basal = (20.315 * peso) + 485.9
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
        elif idade > 10 and idade <= 18:
            if sexo == 'm':
                e_basal = (17.686 * peso) + 658.2
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
            elif sexo == 'f':
                e_basal = (13.384 * peso) + 692.6
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
        elif idade > 18 and idade <= 30:
            if sexo == 'm':
                e_basal = (15.057 * peso) + 692.2
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
            elif sexo == 'f':
                e_basal = (14.818 * peso) + 486.6
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
        elif idade > 30 and idade <= 60:
            if sexo == 'm':
                e_basal = (11.472 * peso) + 873.1
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
            elif sexo == 'f':
                e_basal = (8.126 * peso) + 845.6
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
        elif idade > 60:
            if sexo == 'm':
                e_basal = (11.711 * peso ) + 587.7
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
            elif sexo == 'f':
                e_basal = (9.082 * peso ) + 658.5
                e_basal *= v_exercicio
                b_energetico = calorias_total - e_basal
        print(f'Seu balanço energético diário é: {b_energetico:.2f}\n')

    elif r == '3':
        while True:
            objetivo = input('Deseja emagrecer, manter o peso ou engordar? ')
            objetivo = objetivo.lower()
            if objetivo == 'emagrecer' or objetivo == 'manter o peso' or objetivo == 'engordar':
                break
            else:
                print('Valor inválido')
        '''tabela1 = {'Arroz': 130,
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
                   'Uva': 60}'''
        tabela1 = [['Arroz', 130], ['Feijão', 100], ['Carne', 200], ['Frango', 150], ['Peixe', 100]]
        tabela2 = [['Ovo', 70], ['Leite', 50], ['Queijo', 100], ['Iogurte', 60], ['Batata', 80]]
        tabela3 = [['Abacaxi', 50], ['Maçã', 40], ['Banana', 80], ['Pera', 60], ['Uva', 60]]
        
        refeicao1 = []
        refeicao2 = []
        refeicao3 = []
        print()
        if objetivo == 'emagrecer':
            valor = 0 - e_basal
            contador = 0
            while valor < -500:
                if contador == 5:
                    contador = 0
                # café da manhã
                for refeicao in tabela2:
                    refeicao1.append([tabela2[contador][0], tabela2[contador][1]])
                    valor += tabela2[contador][1]
                    break
                # almoço
                for refeicao in tabela1:
                    refeicao2.append([tabela1[contador][0], tabela1[contador][1]])
                    valor += tabela1[contador][1]
                    break
                # janta
                for refeicao in tabela3:
                    refeicao3.append([tabela3[contador][0], tabela3[contador][1]])
                    valor += tabela3[contador][1]
                    break
                contador += 1

            print('No café da manhã você tem que comer:')
            for refeicao in refeicao1:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')

            print('\nNo almoço você tem que comer:')
            for refeicao in refeicao2:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')

            print('\nNo jantar você tem que comer:')
            for refeicao in refeicao3:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')
            print()
        
        elif objetivo == 'manter o peso':
            valor = 0 - e_basal
            contador = 0
            while valor < 0:
                if contador == 5:
                    contador = 0
                # café da manhã
                for refeicao in tabela2:
                    refeicao1.append([tabela2[contador][0], tabela2[contador][1]])
                    valor += tabela2[contador][1]
                    break
                # almoço
                for refeicao in tabela1:
                    refeicao2.append([tabela1[contador][0], tabela1[contador][1]])
                    valor += tabela1[contador][1]
                    break
                # janta
                for refeicao in tabela3:
                    refeicao3.append([tabela3[contador][0], tabela3[contador][1]])
                    valor += tabela3[contador][1]
                    break
                contador += 1

            print('No café da manhã você tem que comer:')
            for refeicao in refeicao1:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')

            print('\nNo almoço você tem que comer:')
            for refeicao in refeicao2:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')

            print('\nNo jantar você tem que comer:')
            for refeicao in refeicao3:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')
            print()
        
        elif objetivo == 'engordar':
            valor = 0 - e_basal
            contador = 0
            while valor < 500:
                if contador == 5:
                    contador = 0
                # café da manhã
                for refeicao in tabela2:
                    refeicao1.append([tabela2[contador][0], tabela2[contador][1]])
                    valor += tabela2[contador][1]
                    break
                # almoço
                for refeicao in tabela1:
                    refeicao2.append([tabela1[contador][0], tabela1[contador][1]])
                    valor += tabela1[contador][1]
                    break
                # janta
                for refeicao in tabela3:
                    refeicao3.append([tabela3[contador][0], tabela3[contador][1]])
                    valor += tabela3[contador][1]
                    break
                contador += 1

            print('No café da manhã você tem que comer:')
            for refeicao in refeicao1:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')

            print('\nNo almoço você tem que comer:')
            for refeicao in refeicao2:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')

            print('\nNo jantar você tem que comer:')
            for refeicao in refeicao3:
                print(f'{refeicao[0]} com {refeicao[1]} calorias')
            print()