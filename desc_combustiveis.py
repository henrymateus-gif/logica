litros = float(input("Informe a quantidade de litros vendidos: "))
tipo = input("Informe o tipo de combustível (A - Álcool / G - Gasolina): ").upper()

preco_gasolina = 4.95
preco_alcool = 2.89
valor = 0.0

if tipo == 'A':
    if litros <= 20:
        desconto = 0.03
    else:
        desconto = 0.05
    valor = (litros * preco_alcool) * (1 - desconto)
    print(f"Valor a pagar pelo Álcool: R$ {valor:.2f}")
    
elif tipo == 'G':
    if litros <= 20:
        desconto = 0.04
    else:
        desconto = 0.06
    valor = (litros * preco_gasolina) * (1 - desconto)
    print(f"Valor a pagar pela Gasolina: R$ {valor:.2f}")
    
else:
    print("Tipo de combustível inválido!")