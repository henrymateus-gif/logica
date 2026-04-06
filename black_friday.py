preco_total = float(input("Informe o preço total da venda: R$ "))

print("\nFormas de pagamento:")
print("1 - À vista (em espécie) (10% de desconto)")
print("2 - Cartão de débito (5% de desconto)")
print("3 - Cartão de crédito (3% de desconto)")
print("4 - PIX (7.5% de desconto)")
codigo = int(input("\nInforme o código da forma de pagamento (1 a 4): "))

if codigo == 1:
    desconto = 0.10
elif codigo == 2:
    desconto = 0.05
elif codigo == 3:
    desconto = 0.03
elif codigo == 4:
    desconto = 0.075
else:
    desconto = 0
    print("Código inválido! Nenhum desconto será aplicado.")

valor_final = preco_total - (preco_total * desconto)
print(f"O valor final a ser pago é: R$ {valor_final:.2f}")