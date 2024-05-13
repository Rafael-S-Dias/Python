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
    continuar = input("Deseja inserir mais uma nota? [S / N] \n")
    continuar = continuar.upper()
    

    if (continuar == "S"):
        soma += notas
        contador += 1    
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
print(f"Você inseriu {contador} notas")
print(f"A sua media foi: {media}")