# Atividade imprime nome, idade, três notas, média e aprovado.
import os
import array

os.system("cls || clear")

# Variaveis
const = 3

nota = [const]
soma = 0

# Solicitação
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
for i in range (const) :
    nota[i] = float(input(f"Digite sua {i+1}º nota: "))
    soma += nota[i]

# Calculos
media = soma / const

# Exibindo Resultados
os.system("cls || clear")
print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade} anos")
for i in range (const) :
    print(f"Sua {i+1}º nota foi: {nota[i]}")
print(f"Sua média foi: {media}")
if media > 7 :
    print("Parabéns! Você está aprovado.")
else :
    print("Infelizmente você está reprovado")