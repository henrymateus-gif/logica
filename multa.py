velocidade = float(input("Digite a velocidade em Km/h: "))
limite = 80

if velocidade > limite:
    excedeu = velocidade - limite
    multa = excedeu * 50
    print(f"Limite = {limite}Km/h")
    print(f"Excedeu {excedeu:.0f}Km/h")
    print(f"multa = {excedeu:.0f}Km/h * R$ 50,00")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Sua velocidade está dentro do limite permitido.")