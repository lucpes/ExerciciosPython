candidatos = {0: ['nulo', 0], }
brancos = 0
maior = 0
maior2 = 0
while True:
    print('1 - Cadastrar candidato\n2 - Votar\n3 - Resultado\n4 - Sair')
    r = input('Digite a opção desejada: ')
    if r == '1':
        candidato = input('Digite o nome do candidato: ')
        num_candidato = int(input('Digite o número do candidato: '))
        candidatos[num_candidato] = [candidato,0]
        
    elif r == '2':        
        vot_num = input('Digite o número do candidato: ')
        if vot_num == 'branco':
            r2 = input('Confirme o voto em branco (s/n)? ')
            if r2 == 's':
                brancos += 1
            else:
                continue
        elif vot_num == 'nulo':
            r2 = input('Confirme o voto em nulo (s/n)? ')
            if r2 == 's':
                candidatos[0][1] += 1
            else:
                continue
        else:
            vot_num = int(vot_num)
            if vot_num in candidatos.keys():
                r2 = input(f'Confirme o voto em {candidatos[vot_num][0]} (s/n)? ')
                if r2 == 's':
                    candidatos[vot_num][1] += 1
                else:
                    continue
            else:
                r2 = input('Confirme o voto em nulo (s/n)? ')
                if r2 == 's':
                    candidatos[0][1] += 1
                else:
                    continue
    elif r == '3':
        dict_temporario = {}
        sort = []

        for i in candidatos:
            sort.append(i)
        sort.sort()

        for i in sort:
            dict_temporario[i] = [candidatos[i][0], candidatos[i][1]]
        
        

        lista_candidatos = []

        for i in dict_temporario:
            lista_candidatos.append([dict_temporario[i][0], dict_temporario[i][1]])

        listaOrdenada = sorted(lista_candidatos, key = lambda x: x[1], reverse=True)
        
        if listaOrdenada[0][0] == 'nulo':
            listaOrdenada[1][1] += brancos
        else:
            listaOrdenada[0][1] += brancos
        
        listaOrdenada = sorted(lista_candidatos, key = lambda x: x[1], reverse=True)
        
        for i in listaOrdenada:
            print(f'{i[0]}: {i[1]} votos')
        break
    elif r == '4':
        break
