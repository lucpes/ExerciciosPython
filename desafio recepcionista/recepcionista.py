tempo = int(input("Quanto tempo falta para o seu filme? "))

if tempo < -30:
    print("Muito cedo")
elif tempo >= 30:
    print("Atrasado")
else:
    print("Pode entrar")