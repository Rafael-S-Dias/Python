# Atividade obrigatoriedade de votar
import os

os.system("cls || clear")

#Solicitação 
idade =  int(input("Digite sua idade: "))

if idade < 16:
    print("Não permitido votar.")
elif idade < 18:
    print("Voto opcional.")
elif idade < 65:
     print("Voto obrigatório.")
else :
     print("Voto não obrigatório.")