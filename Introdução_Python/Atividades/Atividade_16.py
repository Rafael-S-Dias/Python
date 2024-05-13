# Atividade nota maior que 10 e menor que 1
import os

os.system("cls || clear")

# Variaveis
nota = -1

# Solicitação
while (nota < 0 or nota > 10) :
    nota = float(input("Digite um numero maior que zero e menor que 10: "))