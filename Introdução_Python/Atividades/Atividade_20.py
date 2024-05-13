# Atividade pergunta se inserir nota e media

import os
import time

os.system("cls || clear")

# Variaveis
contador = 1
soma = 0

# Solicitação
while True :
    notas = float(input(f"Digite sua {contador}º nota: "))
    continuar = input("Como deseja prosseguir? \nDigite: \nS para inserir mais uma nota \nP para ver quantas notas foram inseridas\nN para ver a media das notas \n")
    continuar = continuar.upper()
    

    if (continuar == "S"):
        soma += notas
        contador += 1
        os.system("cls || clear")    

    elif (continuar == "P"):
        print(f"Você inseriu {contador} notas")
        soma += notas
        contador += 1
        time.sleep(4)
        os.system("cls || clear") 

    elif (continuar == "N"):
        soma += notas
        break

    else :
        print("COMANDO INVÁLIDO! TENTE NOVAMENTE")
        time.sleep(2)
        os.system("cls || clear")

# Calculos
media = soma / contador

# Exibir Resultados
os.system("cls || clear")
print(f"A sua soma foi: {soma}")
print(f"A sua media foi: {media}")