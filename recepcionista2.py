from dataclasses import replace
from datetime import datetime
data = datetime.now()
h_f = str(input('coloque a hora do filme (Exemplo: 15:30) '))
h_f1 = h_f
h_f = h_f.replace(":", "")

h_at = (int(data.hour))
m_at = (int(data.minute))
h_atual = (h_at*60) + m_at
hora = (h_f[0]) + (h_f[1])
hora = int(hora)
minuto = (h_f[2]) + (h_f[3])
minuto = int(minuto)
hora = hora*60
resultado = hora + minuto
print(resultado)
print(h_atual)
tempo = h_atual - resultado

m_atrasado = m_at - minuto

if tempo < -30:
    print(f"Ainda são {h_at}:{m_at}, muito cedo para seu filme")
elif tempo >= 30:
    print(f"Voce está atrasado, sua sessão começou {h_f1}")
else:
    print("Pode entrar, primeira sala à direita")