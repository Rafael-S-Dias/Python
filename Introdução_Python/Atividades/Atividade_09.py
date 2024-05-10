# Atividade numero e tabuada
import os

os.system("cls || clear")

numero = int(input("Digite o número selecionado: "))

print("===== TABUADA =====")
for i in range(1,11) :
    print(f"{numero} x {i} = {numero * i}")

