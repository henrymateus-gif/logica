texto = input("Digite um texto: ")

# .strip() remove espaços em branco do início e do fim para validar se a string é apenas composta de espaços
if texto.strip() == "":
    print("Dado inválido")
else:
    print(texto)