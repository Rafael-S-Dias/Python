# Atividade nome, sexo e estado civil
import os

os.system("cls || clear")

# Solicitação
nome = input("Digite o seu nome: ")
sexo = input("Informe seu sexo (F OU M): ")
estadoCivil = input("Informe seu estado civil: ")

# Verificação
sexo = sexo.upper()
estadoCivil = estadoCivil.upper()

if sexo == "F" and estadoCivil == "CASADA" :
    tempoCasada = int(input("Informe quantas anos possui de casada: "))

# Exibindo Resultados
os.system("cls || clear")
print(f"Seu nome: {nome}")
if sexo == "F" :
    print("Sexo: Feminino")
else :
    print("Sexo: Masculino")

print(f"Estado civil: {estadoCivil}")
if sexo == "F" and estadoCivil == "CASADA" :
    print(f"Tempo de casada: {tempoCasada}")