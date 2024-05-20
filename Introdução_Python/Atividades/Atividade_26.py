# Atividade 04 notas, media e aprovado

import os
os.system ("clear || cls")

QUANTIDADE_NOTAS = 4
notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Insira sua {i+1}º nota: "))
    notas.append(nota)

media:float = sum(notas) / QUANTIDADE_NOTAS

# Resultados
os.system("clear")
for i, nota in enumerate(notas):
    print(f"{i+1}º nota: {nota}")
print(f"Média: {media}")
if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação!")
else :
    print("Reprovado!")
