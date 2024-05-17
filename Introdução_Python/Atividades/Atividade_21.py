# Atividade vetor

import os
os.system("clear")

notas = []

for i in range (3):
    nota = float(input(f"Digite a nota {i+1}º:"))
    notas.append(nota)


for i, nota in enumerate(notas):
    print(f"{i+1}° nota: {notas[i]}")