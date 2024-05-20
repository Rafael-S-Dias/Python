# Atividade seis notas e pares e impares

import os
os.system("clear")

QUANTIDADE_NOTAS = 6

numeros = []
pares = 0
impares = 0

for i in range (QUANTIDADE_NOTAS):
    numero = float(input(f"Digite a nota {i+1}º: "))
    numeros.append(numero)
    if numero % 2 == 0 :
        pares += 1
    else :
        impares += 1

# Resultado
os.system("clear")
for i, numero in enumerate(numeros):
    print(f"{i+1}° numero: {numero}")
print(f"Quantidade pares: {pares}")
print(f"Quantidade impares: {impares}")
