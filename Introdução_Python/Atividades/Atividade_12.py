# Atividade soma 05 numeros
import os

os.system("cls || clear")

# Variaveis
soma = 0

# Solicitação
for i in range(1,6) :
    numeros = int(input(f"Digite seu {i}º número: "))
    soma += numeros

# Resultados
os.system("cls || clear")
print(f"A soma dos números é: {soma}")