num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
print("5 - Potência\n6 - Raiz quadrada\n7 - Número par\n8 - Número ímpar")

operacao = input("Escolha a operação (1 a 8): ")

if operacao == '1':
    print(f"Resultado: {num1 + num2}")
elif operacao == '2':
    print(f"Resultado: {num1 - num2}")
elif operacao == '3':
    print(f"Resultado: {num1 * num2}")
elif operacao == '4':
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Erro: Divisão por zero!")
elif operacao == '5':
    print(f"Resultado: {num1 ** num2}")
elif operacao == '6':
    print(f"Raiz do 1º número: {num1 ** 0.5}, Raiz do 2º número: {num2 ** 0.5}")
elif operacao == '7':
    print(f"O 1º número {'é' if num1 % 2 == 0 else 'não é'} par.")
    print(f"O 2º número {'é' if num2 % 2 == 0 else 'não é'} par.")
elif operacao == '8':
    print(f"O 1º número {'é' if num1 % 2 != 0 else 'não é'} ímpar.")
    print(f"O 2º número {'é' if num2 % 2 != 0 else 'não é'} ímpar.")
else:
    print("Operação inválida!")