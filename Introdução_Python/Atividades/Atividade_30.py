# Atividade preço e inflação

import os
os.system("clear")

def inflacao(x):
    if x < 100 :
        novo_preco = x + (x * 0.1)
    else :
        novo_preco = x + (x * 0.2)
    return novo_preco

preco = float(input("Digite o valor do produto e veja o seu preço depois da inflação: "))

# Calculos
novo_preco = inflacao(preco)

# Resultados
print(f"Novo preço do produto: {novo_preco}")