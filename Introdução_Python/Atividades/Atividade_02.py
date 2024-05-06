# Atividade imprime nome, idade, três notas, média e aprovado.
import os

os.system("cls || clear")


# Solicitação
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite sua 1º nota: "))
segundaNota = float(input("Digite sua 2º nota: "))
terceiraNota = float(input("Digite sua 3º nota: "))

# Calculos
soma = primeiraNota + segundaNota + terceiraNota
media = soma / 3

# Exibindo Resultados
os.system("cls || clear")
print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade} anos")
print(f"Sua 1º nota foi: {primeiraNota}")
print(f"Sua 2º nota foi: {segundaNota}")
print(f"Sua 3º nota foi: {terceiraNota}")
print(f"Sua média foi: {media}")
if media > 7 :
    print("Parabéns! Você está aprovado.")
else :
    print("Infelizmente você está reprovado")