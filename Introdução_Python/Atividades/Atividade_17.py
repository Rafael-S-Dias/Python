# Atividade duas nota maior que 10 e menor que 1

import os

os.system("cls || clear")

# Variaveis
notas = -1
soma = 0

for i in range(2) : 
    notas = -1
    while (notas < 0 or notas > 10) :
        notas = float(input(f"Digite sua {i+1}º nota, sendo ela maior que zero e menor que 10: "))

        if (notas >= 0 and notas <= 10) :
            soma += notas


# Calculos
media = soma / 2.0

# Exibir Resultados
os.system("cls || clear")
print(f"A sua media foi: {media}")
