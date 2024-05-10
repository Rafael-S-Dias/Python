# Atividade05 numeros pares e impares
import os

os.system("cls || clear")

# Variaveis
pares = 0
impares = 0

for i in range(5) :
    numeros = int(input(f"Digite seu {i+1}º número: "))
    if numeros % 2 == 0:
        pares += 1
    else :
        impares += 1

# Exibir Resultados
os.system("cls || clear")
print(f"Quantidade de numeros pares: {pares}")            
print(f"Quantidade de numeros impares: {impares}")            