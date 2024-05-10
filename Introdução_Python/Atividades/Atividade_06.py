# Atividade nome do produto, a quantidade adquirida e preço unitario
import os

os.system("cls || clear")

# Variaveis
precoMaca = 2.5
precoBanana = 3
precoMorango = 4
produto = 1

# Solicitação
while produto != 1 or produto != 2 or produto != 3 :
    produto = int(input("Qual o produto desejado: (1 = Maça | 2 = Banana | 3 = Morango) : "))

    if produto == 1 :
        precoUnitario = precoMaca
        nomeProduto = "Maça"

    elif produto == 2 :
        precoUnitario = precoBanana
        nomeProduto = "Banana"

    elif produto == 3 : 
        precoUnitario = precoMorango 
        nomeProduto = "Morango"

    else :
        print("Opção não disponivel, tente novamente. ")

    break
quantidadeproduto = int(input("Digite a quantidade a ser comprada: "))


# Desconto
if quantidadeproduto <= 5 :
    desconto = 0.02
elif quantidadeproduto <= 10 :
    desconto = 0.03
else :
    desconto = 0.05

# Calculos
total = quantidadeproduto * precoUnitario
totalPagar = total - (total * desconto)

# Exibindo Resultados
os.system("cls || clear")

print(f"Nome do produto: {nomeProduto}")
print(f"A quantidade: {quantidadeproduto}")
print(f"O valor total foi: {totalPagar}")