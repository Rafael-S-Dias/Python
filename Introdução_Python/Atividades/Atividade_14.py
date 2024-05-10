# Atividade 04 notas e media
import os

os.system("cls || clear")

# Variaveis
soma = 0

# Solicitação
for i in range(4) :
    notas = float(input(f"Digite seu {i+1}º nota: "))
    soma += notas

# Calculos
media = soma / 4.0

# Exibir Resultados
os.system("cls || clear")
print(f"A sua media foi: {media}")
