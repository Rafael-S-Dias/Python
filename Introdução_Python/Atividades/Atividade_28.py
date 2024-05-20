# Atividade 5 numeros com função

import os
os.system("clear")

QUANTIDADE_NUMEROS = 5
numeros = []
def pergunta (i):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero < 0:
        numero = 0
    numeros.append(numero)


for i in range(QUANTIDADE_NUMEROS) :
    pergunta (i)  

# Resultados
print(f"Os números foram: {numeros}")