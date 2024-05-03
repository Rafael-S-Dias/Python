# Atividade imprime nome, idade, duas notas e média.
import os
import array

os.system("cls || clear")

# Variaveis
nota = [1,2]
soma = 0

# Solicitação
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
for i in range (2) :
    nota[i] = float(input(f"Digite sua {i+1}º nota: "))
    soma += nota[i]

# Calculos
media = soma / 2

# Exibindo Resultados
os.system("cls || clear")
print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade} anos")
for i in range (2) :
    print(f"Sua {i+1}º nota foi: {nota[i]}")
print(f"Sua média foi: {media}")
