# Atividade 03 notas, media e aprovado
import os

os.system("cls || clear")

# Variaveis
soma = 0

# Solicitação
for i in range(3) :
    notas = float(input(f"Digite seu {i+1}º nota: "))
    soma += notas

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