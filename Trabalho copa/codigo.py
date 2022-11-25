import random
#Pontos = {'A':[],'B':[],'C':[],'D':[''],'E':[],'F':[],'G':[],'H':[]}
Oceania = ['Australia']
Cabeça = ['Catar','Brasil','Argentina','Bélgica','Inglaterra','França','Espanha','Portugal']
Europa = ['Croacia','Holanda','Gales','Polania','Dinamarca','Alemanha','Servia','Suiça']
Asia = ['Japao','Coreia Sul']
Africa = ['Gana','Camaroes','Arabia Saudita','Senegal','Marrocos','Irâ','Tunisia']
America = ['Equador','Mexico','Uruguai','Costa Rica','Canada', 'Estados Unidos']
Grupos = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[]}
chaves = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
def vencedor(chave, time1, time2):
    random.seed()
    r1 = (random.sample([0, 1, 2], k=1)) # 0 = empate, 1 = ganhador 1 e 2 = ganhador 2
    if time1 == 'Brasil' or time2 == 'Brasil': # codigo para o brasil ganhar
        if time1 == 'Brasil':
            chave[time1] += 3
        elif time2 == 'Brasil':
            chave[time2] += 3
    elif r1[0] == 0:
        chave[time1] += 1
        chave[time2] += 1
    elif r1[0] == 1:
        chave[time1] += 3
    elif r1[0] == 2:
        chave[time2] += 3
def aleatorio(classe):

    random.seed()
    g2 = (random.sample(classe, k=len(classe)))
    x = 0
    for chave in chaves:
        if x == len(classe):
            break
        Grupos[chave].append(g2[x])
        #Pontos[chave].append([0, g2[x]])
        x += 1
aleatorio(Cabeça)
aleatorio(Europa)
aleatorio(Africa)
aleatorio(America)

random.seed()
g1 = (random.sample(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], k=8))
x = 0
for y in g1:
    if len(Grupos[g1[x]]) >= 4:
        x += 1
    else:
        Grupos[g1[x]].append('Japao')
        #Pontos[g1[x]].append([0, 'Japao'])
        break
for y in g1:
    if len(Grupos[g1[x]]) >= 4:
        x += 1
    else:
        Grupos[g1[x]].append('Australia')
        #Pontos[g1[x]].append([0, 'Australia'])
        break
for y in g1:
    if len(Grupos[g1[x]]) >= 4:
        x += 1
    else:
        Grupos[g1[x]].append('Coreia do Sul')
        #Pontos[g1[x]].append([0, 'Coreia do Sul'])
        break

# Parte 2
jogos = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[]}
n = 0
for chave in chaves:
    jogostemp = []
    for x in Grupos[chave]:
        for y in Grupos[chave]:
            if x == y:
                continue
            jogostemp.append([x, y])
    for i, x in enumerate(jogostemp):
        jogostemp[i].sort()
    jogostemp.sort()
    for x in jogostemp:
        if x not in jogos[chave]:
            jogos[chave].append(x)
#Parte 3

PA = {}
PB = {}
PC = {}
PD = {}
PE = {}
PF = {}
PG = {}
PH = {}

for chave in chaves:
    for x in Grupos[chave]:
        if chave == 'A':
            PA[x] = 0
        if chave == 'B':
            PB[x] = 0
        if chave == 'C':
            PC[x] = 0
        if chave == 'D':
            PD[x] = 0
        if chave == 'E':
            PE[x] = 0
        if chave == 'F':
            PF[x] = 0
        if chave == 'G':
            PG[x] = 0
        if chave == 'H':
            PH[x] = 0

for chave in chaves:
    for x in jogos[chave]:
        if chave == 'A':
            vencedor(PA, x[0], x[1])
        if chave == 'B':
            vencedor(PB, x[0], x[1])
        if chave == 'C':
            vencedor(PC, x[0], x[1])
        if chave == 'D':
            vencedor(PD, x[0], x[1])
        if chave == 'E':
            vencedor(PE, x[0], x[1])
        if chave == 'F':
            vencedor(PF, x[0], x[1])
        if chave == 'G':
            vencedor(PG, x[0], x[1])
        if chave == 'H':
            vencedor(PH, x[0], x[1])
print('Pontuação na fase de grupo')
print(PA)
print(PB)
print(PC)
print(PD)
print(PE)
print(PF)
print(PG)
print(PH)
print()
# Oitavas
oitavas1 = []
oitavas2 = []
quartas = []
semi = []
final = []
ganhador = []
def oitavas(ChaveP):
    x = 0
    for i in sorted(ChaveP, key = ChaveP.get, reverse=True):
        if x == 0:
            oitavas1.append(i)
        if x == 1:
            oitavas2.append(i)
        x += 1
oitavas(PA)
oitavas(PB)
oitavas(PC)
oitavas(PD)
oitavas(PE)
oitavas(PF)
oitavas(PG)
oitavas(PH)
print()
print('Oitavas de final')
print()

def vencedor2(posicao, time1, time2):
    '''vencedor do mata-mata'''
    print(f'{time1} x {time2}')
    random.seed()
    r1 = (random.sample([1, 2], k=1))  # 1 = ganhador 1 e 2 = ganhador 2
    if time1 == 'Brasil' or time2 == 'Brasil':  # codigo para o brasil ganhar
        if time1 == 'Brasil':
            posicao.append('Brasil')
            print(f'{time1} foi o vencedor')
        elif time2 == 'Brasil':
            posicao.append('Brasil')
            print(f'{time2} foi o vencedor')
    elif r1[0] == 1:
        posicao.append(time1)
        print(f'{time1} foi o vencedor')
    elif r1[0] == 2:
        posicao.append(time2)
        print(f'{time2} foi o vencedor')

n1 = 0
n2 = 1
for x in range(1, 5):
    vencedor2(quartas, oitavas1[n1], oitavas1[n2])
    vencedor2(quartas, oitavas2[n1], oitavas2[n2])
    n1 += 2
    n2 += 2
# Quartas de final
print()
print('Quartas de final')
print()
n1 = 0
n2 = 1
for x in range(1, 5):
    vencedor2(semi, quartas[n1], quartas[n2])
    n1 += 2
    n2 += 2

# Semi final
print()
print('Semi Final')
print()
n1 = 0
n2 = 1
for x in range(1, 3):
    vencedor2(final, semi[n1], semi[n2])
    n1 += 2
    n2 += 2
print()
print('Final')
print()
vencedor2(ganhador, final[0], final[1])