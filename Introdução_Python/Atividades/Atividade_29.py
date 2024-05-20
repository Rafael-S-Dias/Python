# Atividade 2 numeros e retorne soma, sub, mult e div

import os
os.system("clear")

QUANTIDADE_NUMERO = 2
numeros = []
def operacao(x, y):
    soma = x + y
    sub = x - y
    mult = x * y
    div = x / y
    return soma, sub, mult, div

for i in range(QUANTIDADE_NUMERO):
    numero = float(input(f"Insira seu {i+1}º número: "))
    numeros.append(numero)

# Calculos
somar, subtrair, multiplicar, dividir = operacao(numeros[0], numeros[1])

# Resultados
print(f"Números informados: {numeros}")
print(f"Soma: {somar}")
print(f"Subtrair: {subtrair}")
print(f"Multiplicação: {multiplicar}")
print(f"Divisão: {dividir}")


