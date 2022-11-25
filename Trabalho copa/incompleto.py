import random

# Parte 2
'''grupo1 = ['Brasil', 'Camaroes', 'Suiça', 'Sérvia']
jogostemp = []
jogos = []
n = 0
for x in grupo1:
    for y in grupo1:
        if x == y:
            continue
        jogostemp.append([x, y])
for i, x in enumerate(jogostemp):
    jogostemp[i].sort()
jogostemp.sort()
for x in jogostemp:
    if x not in jogos:
        jogos.append(x)
print(jogos)

# Parte 2
pontuaçao = {}
for x in grupo1:
    pontuaçao[x] = 0
print(pontuaçao)
for x in jogos:
    r = input(f'Vencedor do jogo do {x[0]} x {x[1]}: (ou empate) ')
    if r == x[0]:
        pontuaçao[x[0]] += 3
    elif r == x[1]:
        pontuaçao[x[1]] += 3
    elif r == 'empate':
        pontuaçao[x[0]] += 1
        pontuaçao[x[1]] += 1
'''
# Parte 4
pontuaçao = {'Brasil': 9, 'Camaroes':3, 'Suiça': 4, 'Sérvia': 0}
print(pontuaçao)
potetemp = []
pote1 = [[0, 'Uruguai'], [0, 'Portugal'], [0, 'França'], [0, 'Argentina'], [0, 'México'], [0, 'Belgica'], [0, 'Japão']]
pote2 = [[0, 'Espanha'], [0,'Rússia'], [0, 'Croácia'], [0, 'Dinamica'], [0, 'Suécia'], [0, 'Colombia'], [0, 'Inglaterra']]
for k, v in pontuaçao.items():
    potetemp.append([v, k])
potetemp.sort(reverse=True)
pote1.append(potetemp[0])
pote2.append(potetemp[1])
oitavas = []
n1 = 0
n2 = 1
for x in range(1, 5):
    oitavas.append([pote1[n1], pote1[n2]])
    oitavas.append([pote2[n1], pote2[n2]])
    n1 += 2
    n2 += 2
print(oitavas)
jogos_oitava = []
for i, x in enumerate(oitavas):
    jogos_oitava.append([i[0][0], i[0][1]])
    print(jogos_oitava)

