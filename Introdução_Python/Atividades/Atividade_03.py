# Atividade imprime nome, idade, três numeross, média e aprovado.
import os
import array

os.system("cls || clear")

# Variaveis
const = 2

numeros = [const]
soma = 0
maior_valor = 0
menor_numero = 0


#Solicitação
for i in range(const) :
    numeros = int(input(f"Digite seu {i+1}º numero: "))
    soma += numeros


# Maior e Menor numeros
maior = max(numeros[1], numeros[2])
menor = min(numeros[1], numeros[2])

# Calculos
produto = numeros[1] * numeros[2]
media = soma / const

# Exibindo Resultados
os.system("cls || clear")
for i in range(const) :
    print(f"Seu {i+1}º numero foi: {numeros[i]}")
print(f"Sua soma foi: {soma}")
print(f"Sua media foi: {media}")
print(f"O produto desses numeros foi: {produto}")
print(f"O maior número é: {maior_valor}")
print(f"O menor número é: {menor_numero}")
