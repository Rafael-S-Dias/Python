# Atividade lista com 10 numeros, positivos e negativos 

import os
os.system("clear || cls")

QUATIDADE_NUMEROS = 10
numeros = []
soma = 0
negativos = 0

for i in range(QUATIDADE_NUMEROS):
    numero = float(input(f"Digite seu {i+1}º numero real: "))
    numeros.append(numero)
    if numero > 0:
        soma += numero
    elif numero < 0:
        negativos += 1

# Resultados
os.system("clear || cls")
for i, numero in enumerate(numeros) :
    print(f"{i+1}º numero: {numero}")
print(f"A soma dos numeros positivos inseridos: {soma}")
print(f"Quantidade de numeros negativos: {negativos}")