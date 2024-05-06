# Atividade imprime nome, idade, duas notas e média.
import os

os.system("cls || clear")

# Solicitação
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeiraNota = float(input(f"Digite sua 1º nota: "))
segundaNota = float(input(f"Digite sua 2º nota: "))

# Calculos
soma = primeiraNota + segundaNota
media = soma / 2


# Exibindo Resultados
os.system("cls || clear")
print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade} anos")
print(f"Sua 1º nota foi: {primeiraNota}")
print(f"Sua 2º nota foi: {segundaNota}")
print(f"Sua média foi: {media}")
