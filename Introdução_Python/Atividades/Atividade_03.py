# Atividade imprime dois numeros, soma, media, produto, maior e menor valor
import os

os.system("cls || clear")

#Solicitação
primeiroNumero = float(input("Digite sua 1º numero: "))
segundoNumero = float(input("Digite sua 2º numero: "))


# Maior e Menor numeros
if primeiroNumero > segundoNumero :
    maiorValor = primeiroNumero
    menorValor = segundoNumero
elif segundoNumero < primeiroNumero :
    maiorValor = segundoNumero
    menorValor = primeiroNumero
else :
    print(f"Primeiro e segundo numeros tem o mesmo valor!")


# Calculos
soma = primeiroNumero + segundoNumero
produto = primeiroNumero * segundoNumero
media = soma / 2

# Exibindo Resultados
os.system("cls || clear")

print(f"Sua soma foi: {soma}")
print(f"Sua media foi: {media}")
print(f"O produto desses numeros foi: {produto}")
print(f"O maior número é: {maiorValor}")
print(f"O menor número é: {menorValor}")
