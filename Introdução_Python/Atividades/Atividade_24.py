# Atividade cinco notas e maior e menor

import os
os.system("clear")

QUANTIDADE_NOTAS = 5

numeros = []

for i in range (QUANTIDADE_NOTAS):
    numero = float(input(f"Digite a nota {i+1}º: "))
    numeros.append(numero)

# Maior e Menor numero
maior_numero = max(numeros)
menor_numero = min(numeros)

# Resultado
os.system("clear")
for i, numero in enumerate(numeros):
    print(f"{i+1}° numero: {numero}")
print(f"Maior numero: {maior_numero}")
print(f"Menor numero: {menor_numero}")