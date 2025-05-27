from tkinter import *
from tkinter import messagebox
import banco
menu_inicial = Tk()

def entrar():
    nome = txtUsuario.get()
    senha = txtSenha.get()
    print(f"Usuário: {nome} - Senha: {senha}")
    banco.salvar(nome, senha)


def cancelar():
    resposta = messagebox.askyesno("Sair do sistema", "Deseja sair do sistema?")
    if resposta == True:
        messagebox.showinfo("Sair", "Sistema fechado!")
        menu_inicial.destroy()

#showinfo, askshowwarning, showerror, askyesno, askokcancel
menu_inicial.title("Exemplo de interface")
menu_inicial.resizable(True, True)
menu_inicial.geometry("500x500+500+150")

#fg = foreground = cor da letra
label1 = Label (menu_inicial, text= "Login:", fg = "red", font = "Arial 20 bold")
label1.grid(row=0, column=0, padx=5, pady=10, sticky=W)
label1 = Label (menu_inicial, text= "Senha:", fg = "red", font = "Arial 20 bold")
label1.grid(row=1, column=0, padx=5, pady=10, sticky=W)

txtUsuario = Entry(menu_inicial, font = "Arial 20 bold")
txtUsuario.grid(row=0, column=1, padx=5, pady=10,sticky=W)

txtSenha = Entry(menu_inicial, font = "Arial 20 bold", show='*')
txtSenha.grid(row=1, column=1, padx=5, pady=10,sticky=W)

btExecutar = Button (menu_inicial, text= "Entrar", bg = "green", fg = "yellow", font = "Arial 15", command= entrar)
btExecutar.grid(row=2, column=1, padx=0, pady=10, sticky=W)

btCancelar = Button (menu_inicial, text= "Sair", bg = "yellow", fg = "red", font = "Arial 15", command= cancelar)
btCancelar.grid(row=2, column=1, padx=0, pady=10, sticky=E)

menu_inicial.mainloop()