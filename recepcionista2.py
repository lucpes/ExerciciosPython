from dataclasses import replace
from datetime import datetime
data = datetime.now()

while True:
    h_f = str(input('coloque a hora do filme (Exemplo: 15:30) '))
    h_f = h_f.replace(":", "")
    if len(h_f) != 4:
        print("Horário inválido")
        continue
    break

h_at = (int(data.hour))
m_at = (int(data.minute))
h_atual = (h_at*60) + m_at
hora = (h_f[0]) + (h_f[1])
hora = int(hora)
minuto = (h_f[2]) + (h_f[3])
minuto = int(minuto)
hora = hora*60
resultado = hora + minuto
tempo = h_atual - resultado

h_rest = h_at - int(h_f[0] + h_f[1])
m_rest = m_at - int(h_f[2] + h_f[3])
if m_rest < 0:
    h_rest -= 1
    m_rest += 60

if tempo < -30:
    print(f"Ainda são {h_at}:{m_at}, muito cedo para seu filme.")
elif tempo >= 30:
    print(f"Voce está atrasado em {h_rest} hora(s) e {m_rest} minutos, as portas já fecharam.")
else:
    print("Pode entrar, primeira sala à direita.")