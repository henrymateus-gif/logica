print("******************************")
print("CÁLCULO DE GRANDEZAS ELÉTRICAS")
print("******************************")
print("1. Tensão (em Volt)")
print("2. Resistência (em Ohm)")
print("3. Corrente (em Ampére)")
print("4. Sair do programa")
print("******************************")

opcao = int(input("Qual grandeza deseja calcular? "))

if opcao == 1:
    r = float(input("Informe o valor da Resistência (em Ohm): "))
    i = float(input("Informe o valor da Corrente (em Ampére): "))
    u = r * i
    print(f"O valor da Tensão é: {u} V")
elif opcao == 2:
    u = float(input("Informe o valor da Tensão (em Volt): "))
    i = float(input("Informe o valor da Corrente (em Ampére): "))
    r = u / i
    print(f"O valor da Resistência é: {r} Ώ")
elif opcao == 3:
    u = float(input("Informe o valor da Tensão (em Volt): "))
    r = float(input("Informe o valor da Resistência (em Ohm): "))
    i = u / r
    print(f"O valor da Corrente é: {i} A")
elif opcao == 4:
    print("Saindo do programa...")
else:
    print("Opção inválida!")