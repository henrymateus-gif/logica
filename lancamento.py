import time # Opcional: apenas para adicionar um pequeno atraso (delay) entre os números

for i in range(10, -1, -1):
    print(i)
    time.sleep(1) # Aguarda 1 segundo (comente ou remova esta linha se quiser imediato)

print("Ignição!")