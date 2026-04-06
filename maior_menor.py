num1 = float(input("num1 = "))
num2 = float(input("num2 = "))
num3 = float(input("num3 = "))

print("**********")

numeros = [num1, num2, num3]
maior = max(numeros)
menor = min(numeros)
soma = sum(numeros)
media = soma / 3

# Usando int() na formatação para bater exatamente com o exemplo se não tiver decimais
print(f"maior = {maior:g}")
print(f"menor = {menor:g}")
print(f"soma = {soma:g}")
print(f"media = {media:g}")