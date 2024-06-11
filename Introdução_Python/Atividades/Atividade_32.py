import os
from dataclasses import dataclass

os.system("clear || cls")

QUANTIDADE_LIVROS = 2

@dataclass
class Livro:
    titulo: str
    autor: str
    paginas: int
    preco: float

livros = []

for i in range(QUANTIDADE_LIVROS):
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    paginas = int(input("Digite a quantidade de paginas: "))
    preco = float(input("Digite o preço em reais: "))
    livro = Livro(titulo = titulo, autor = autor, paginas = paginas, preco = preco)
    livros.append(livro)

for dados_livros in livros:
    print(f"Título: {dados_livros.titulo}")
    print(f"Nome do autor: {dados_livros.autor}")
    print(f"Número de paginas: {dados_livros.paginas}")
    print(f"Preço: {dados_livros.preco} Reais")