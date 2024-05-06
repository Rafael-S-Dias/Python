# Atividade login e senha
import os

os.system("cls || clear")

#Variaveis
login = "Rafael"
senha = 1234

#Solicitação
loginTentativa = input("Digite seu login: ")
senhaTentativa = int(input("Digite sua senha: "))
os.system("cls || clear")

if login == loginTentativa and senha == senhaTentativa :
    print(f"Bem vindo {login}!")
else :
    print("Login e/ou senha incorretos!")  
