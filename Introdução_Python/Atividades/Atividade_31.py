import os
from dataclasses import dataclass

os.system("clear || cls")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade: int
    peso: float
    altura: float

alunos = []

for i in range(QUANTIDADE_ALUNOS):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))
    aluno = Aluno(nome = nome, idade = idade, peso = peso, altura = altura)
    alunos.append(aluno)

for dados_alunos in alunos:
    print(f"Nome: {dados_alunos.nome}")
    print(f"Idade: {dados_alunos.idade} Anos")
    print(f"Peso: {dados_alunos.peso} Kgs")
    print(f"Altura: {dados_alunos.altura} Metros")