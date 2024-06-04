import os
import time
os.system("cls || clear")

#VARIÁVEIS.
login_cadastrado = "O CARA"
senha_cadastrada = "1234"
dinheiro = 8000.00
saque_nome = "Saque"
transferencia_nome = "Transferência"
deposito_nome = "Deposito"
pagamento_nome = "Pagamento"

# FUNÇÕES.
def logo_banco():
    print("=" * 50)
    print("                 BANCO DOS CARAS        ")
    print("=" * 50)
    
def bem_vindo():
    tentativa = 1
    while tentativa <= 3:
        login = input("Insira seu login: ")
        senha = input("Digite sua senha: ")
        if login.upper() == login_cadastrado and senha == senha_cadastrada:
            print("                   BEM VINDO!                             ")
            return True
            
        elif login.upper() != login_cadastrado:  
            print("Login incorreto. Tente novamente!")
            time.sleep(3)
            os.system("clear || cls")
            tentativa +=1
            
        elif senha != senha_cadastrada: 
            print("Senha incorreta. Tente novamente!")
            time.sleep(3)
            os.system("clear || cls")
            tentativa += 1
              
        elif senha != senha_cadastrada and login.upper() != login_cadastrado: 
            print("Login e Senha incorreta. Tente novamente!")
            time.sleep(3)
            os.system("clear || cls")
            tentativa += 1

    if tentativa == 4:
        print("Você excedeu o número de tentativas! ")
        time.sleep(2)
        return False

def senha(x):            
    tentativa = 1
    while tentativa <= 3:
        senha = input("Digite sua senha: ")
        if senha == senha_cadastrada:
            tela_de_load()
            print(f"{x} Realizado com sucesso!")
            time.sleep(2)
            return True
        if senha != senha_cadastrada: 
            print("Senha incorreta. Tente novamente!")
            print(f"{tentativa} de 3 tentativas")
            time.sleep(2)
            tentativa += 1
    if tentativa == 4:
        print("Você excedeu o número de tentativa ")
        time.sleep(2)
        return False
               
def saldo():
    os.system("clear || cls")
    print("Saldo em conta ................. R$",round (dinheiro,2), "Reais")
    time.sleep(3)
    os.system("clear || cls")      


def menu():
    print("1 - Saque")
    print("2 - Saldo")
    print("3 - Pix / Transferência")
    print("4 - Pagamento")
    print("5 - Depósito")
    print("6 - Sair")
    banco = int (input("Selecione uma opção desejada: "))
    return banco


def saque():
    global dinheiro
    os.system("clear || cls")
    print('=== Área Saque ===  ')
    valor = float(input("Informe o valor referente do saque: R$ "))
    if valor < dinheiro :
        os.system("clear || cls")
        print("Revise o valor do saque: ")
        print(f"Saque desejado: R${valor}")
        confirmacao = input("O valor está correto? \nDIGITE [S] PARA CONFIRMAR OU QUALQUER OUTRA TECLA PARA REPETIR: ")
        if confirmacao.upper() == "S":
            os.system("clear || cls")
            if senha(saque_nome):
                dinheiro -= valor
            os.system("clear || cls")
        else :
            os.system("clear || cls")
            saque()
    else :
            os.system("clear || cls")
            print("Saldo insuficiente! Tente novamente!")
            time.sleep(2)
            os.system("clear || cls")
            saque()

    return dinheiro


def central_de_transferencia():
    global dinheiro
    print('  === Área pix ===')
    print('Digite (1) para transferir')
    print('Digite (2) para Ler QR code')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        transferencia = float(input('Qual o valor da transferência? '))
        os.system("clear || cls")
        if transferencia > 0:
            print("Dica: gabriel")
            paraquem = input(f'Para quem você quer transferir R${transferencia} Reais: ').lower()
            if paraquem == "gabriel":
                if senha(transferencia_nome):
                    dinheiro -= transferencia
            else:
                print('Usuário não encontrado.')
                central_de_transferencia()

    elif opcao == 2: 
        print('Aponte a câmera para o QR code para realizar o pagamento\n')
        time.sleep(3)
        print ('──────▄▄▄▄▄███████████████████▄▄▄▄▄──────')
        print('────▄██████████▀▀▀▀▀▀▀▀▀▀██████▀████▄────')
        print('──▄██▀████████▄─────────────▀▀████─▀██▄──')
        print('─▀██▄▄██████████████████▄▄▄─────────▄██▀─')
        print('───▀█████████████████████████▄────▄██▀───')
        print('─────▀████▀▀▀▀▀▀▀▀▀▀▀▀█████████▄▄██▀─────')
        print('───────▀███▄──────────────▀██████▀───────')
        print('─────────▀██████▄─────────▄████▀─────────')
        print('────────────▀█████▄▄▄▄▄▄▄███▀────────────')
        print('──────────────▀████▀▀▀████▀──────────────')
        print('────────────────▀███▄███▀────────────────')
        print('───────────────────▀█▀───────────────────')
    return dinheiro


def deposito():
    global dinheiro
    os.system("clear || cls")
    print('=== Área Depósito ===  ')
    valor = float(input("Informe o valor referente ao deposito: R$ "))
    os.system("clear || cls")
    print("Revise o valor do depósito: ")
    print(f"Depósito desejado: R${valor}")
    confirmacao = input("O valor está correto? \nDIGITE [S] PARA CONFIRMAR OU QUALQUER OUTRA TECLA PARA REPETIR: ")
    if confirmacao.upper() == "S":
        os.system("clear || cls")
        if senha(deposito_nome):
            dinheiro += valor
    
    else :
        os.system("clear || cls")
        deposito()

    return dinheiro


def tela_de_load(): 
    os.system ('cls || clear')     
    print('PROCESSANDO DADOS.')
    time.sleep(0.8)    
    os.system ('cls || clear')
    print('PROCESSANDO DADOS..')
    time.sleep(0.8)
    os.system ('cls || clear')
    print('PROCESSANDO DADOS...')
    time.sleep(0.8)
    os.system ('cls || clear')    
    print('PROCESSANDO DADOS....')
    time.sleep(0.8)
    os.system ('cls || clear')
    print('PROCESSANDO DADOS.')
    time.sleep(0.8)
    os.system ('cls || clear')
    print('PROCESSANDO DADOS..')
    time.sleep(0.8)


def scanear():
    print("           Leitura é automática.                ")
    print(" ================================================")
    print("|                                                |")
    print("| -----------------------------------------------|")
    print("|                                                |")
    print(" ================================================")


def pagamento():
    while True:
        print("          PAGAMENTO          ")
        print(" BOLETO, CONTAS OU TRIBUTOS")
        
        print("\n")    
        print("       PAGAMENTOS       ")
        print("1 - ESCANEAR")
        print("2 - DIGITAR")
        pagamento = int(input("Escolha uma opção: "))
        if pagamento == 1:
            if pagamento == 1:
                scanear()
        elif pagamento == 2:
            print("       CÓDIGO DE BARRAS       ")
            print("Digite o código de barra do boleto que quer realizar o pagamento")
            codigo = float (input("Digite o código: ")) 
            codigo = input("Deseja proceguir (s/n):")
            if codigo.upper() == "S":
                os.system("clear || cls")
                senha(pagamento_nome)
                time.sleep(3)


def menu_escolha():
    menu_banco = menu()

    while menu_banco != 6:
        if menu_banco == 1:
            saque()

        elif menu_banco == 2:  
            saldo()
                
        elif menu_banco == 3:
            central_de_transferencia()
                
        elif menu_banco == 4:
            pagamento()

        elif menu_banco == 5:
            deposito()

        elif menu_banco == 6:
            exit()

        else :
            print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE!")
            time.sleep(2)
            os.system("clear || cls")
        menu_banco = menu()



# Solicitação
logo_banco()
time.sleep(2)
os.system("clear || cls")

if bem_vindo():
    time.sleep(2)
    os.system("clear || cls")

    menu_escolha()



