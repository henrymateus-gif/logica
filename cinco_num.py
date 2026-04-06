numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("\nOs números digitados foram:")
for n in numeros:
    print(n)