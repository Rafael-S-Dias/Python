# Atividade dois inteiros e operação com match case
import os

os.system("cls || clear")

# Solicitação
primeiroNumero = int(input("Digite o valor de A numero: "))
segundoNumero = int(input("Digite o valor de B numero: "))
operacao = input("Selecione a operação desejada: ")

match(operacao): 
    case "+" :
        resultado = primeiroNumero + segundoNumero

    case "-" :
        resultado = primeiroNumero - segundoNumero

    case "*" :
        resultado = primeiroNumero * segundoNumero

    case "/" :
        resultado = primeiroNumero / segundoNumero


# Exibir Resultado
os.system("cls || clear")
print(f"Resultado: {primeiroNumero} {operacao} {segundoNumero} = {resultado}")

