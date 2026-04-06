entrada = input("Digite um número inteiro: ")

if entrada.strip() == "":
    print("Dado inválido")
else:
    try:
        numero = int(entrada)
        print(numero)
    except ValueError:
        print("Dado inválido")