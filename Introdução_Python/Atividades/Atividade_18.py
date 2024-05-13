# Atividade três notas maior que 10 e menor que 1, mostrar media e se está aprovado

import os

os.system("cls || clear")

# Variaveis
notas = -1
soma = 0

for i in range(3) : 
    while True:
        notas = float(input(f"Digite sua {i+1}º nota, sendo ela maior que zero e menor que 10: "))

        if (notas < 0 or notas > 10) :
            print("Nota inválida! \n")
        else:
            soma += notas
            break


# Calculos
media = soma / 3.0

# Exibir Resultados
os.system("cls || clear")
print(f"A sua media foi: {media}")
if media >= 7: 
    print("Você está aprovado!")
elif media >= 4 and media < 7 :
    print("Você está de recuperação!")
else :
    print("Você está reprovado!")
