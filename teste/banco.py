def salvar(nome, senha):
    with open("banco.txt", "w") as arquivo:
        arquivo.write(f"Usuário: {nome} - Senha: {senha}\n")

