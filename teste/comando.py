from tkinter import *
from tkinter import messagebox
menu_inicial = Tk()

def executar():
    messagebox.showinfo("Informação!", "Função executar chamada!")


def cancelar():
    messagebox.askokcancel("Pergunta", "Você quer cancelar?")

#showinfo, askshowwarning, showerror, askyesno, askokcancel
menu_inicial.title("Exemplo de interface")
menu_inicial.resizable(True, True)
menu_inicial.geometry("300x250+500+200")

#fg = foreground = cor da letra
label1 = Label (menu_inicial, text= "Primeiro Rótulo", bg = "blue", fg = "black", font = "Times 20 bold")
label1.pack()
botao1 = Button (menu_inicial, text= "Executar", bg = "green", fg = "yellow", font = "Times 15 normal", command= executar)
botao1.pack()
label2 = Label (menu_inicial, text= "Segundo Rótulo", bg = "#0e91c4", fg = "white", font = "Times 20 bold")
label2.pack()
botao1 = Button (menu_inicial, text= "Cancelar", bg = "red", fg = "white", font = "Times 15 normal", command= cancelar)
botao1.pack()

menu_inicial.mainloop()