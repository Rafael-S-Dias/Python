# Atividade tres notas e media

import os
os.system("clear")

QUANTIDADE_NOTAS = 3

notas = []
soma = 0

for i in range (QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a nota {i+1}º: "))
    notas.append(nota)

# Calculos
media = sum(notas) / QUANTIDADE_NOTAS

# Resultado
os.system("clear")
for i, nota in enumerate(notas):
    print(f"{i+1}° nota: {nota}")
print(f"Media: {media}")