'''
===============================
EXERCÍCIO 1 - BOLETIM ESCOLAR
===============================


aluno = {}

nome = input("Nome do aluno: ")
media = float(input("Média: "))

if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

aluno["nome"] = nome
aluno["media"] = media
aluno["situacao"] = situacao

print(aluno)
'''


'''
===============================
EXERCÍCIO 2 - JOGO DE DADOS
===============================

import random
jogadores = {}

for i in range(1, 5):
    valor = random.randint(1, 6)
    jogadores[f"Jogador {i}"] = valor

print("\nValores sorteados:")
for j, v in jogadores.items():
    print(j, "tirou", v)

ranking = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

print("\nRanking:")
for pos, item in enumerate(ranking, start=1):
    print(pos, "-", item[0], "com", item[1])

'''

'''
===============================
EXERCÍCIO 3 - CADASTRO TRABALHADOR
===============================

from datetime import datetime
pessoa = {}

pessoa["nome"] = input("Nome: ")
ano = int(input("Ano de nascimento: "))
pessoa["idade"] = datetime.now().year - ano

ctps = int(input("Carteira de trabalho (0 se não tem): "))
pessoa["ctps"] = ctps

if ctps != 0:
    pessoa["ano_contratacao"] = int(input("Ano de contratação: "))
    pessoa["salario"] = float(input("Salário: "))
    pessoa["aposentadoria"] = pessoa["idade"] + 35

print(pessoa)
'''


'''
===============================
EXERCÍCIO 4 - CONTROLE DE JOGADOR
===============================


jogador = {}

jogador["nome"] = input("Nome do jogador: ")
partidas = int(input("Quantas partidas jogou? "))

gols = []

for i in range(partidas):
    gol = int(input(f"Gols na partida {i+1}: "))
    gols.append(gol)

jogador["gols"] = gols
jogador["total"] = sum(gols)

print(jogador)

'''

'''
===============================
EXERCÍCIO 5 - ANÁLISE DE PESSOAS
===============================


pessoas = []
soma = 0
mulheres = []

while True:

    pessoa = {}

    pessoa["nome"] = input("Nome: ")
    pessoa["sexo"] = input("Sexo (M/F): ")
    pessoa["idade"] = int(input("Idade: "))

    soma += pessoa["idade"]

    if pessoa["sexo"] == "F":
        mulheres.append(pessoa["nome"])

    pessoas.append(pessoa)

    continuar = input("Quer continuar? (S/N): ")

    if continuar == "N":
        break

media = soma / len(pessoas)

print("\nTotal de pessoas:", len(pessoas))
print("Média de idade:", media)
print("Mulheres:", mulheres)

print("\nPessoas acima da média:")
for p in pessoas:
    if p["idade"] > media:
        print(p["nome"], p["idade"])

'''

'''
===============================
EXERCÍCIO 6 - APRIMORANDO FUTEBOL
===============================


time = []

while True:

    jogador = {}

    jogador["nome"] = input("Nome do jogador: ")
    partidas = int(input("Quantas partidas jogou: "))

    gols = []
    for i in range(partidas):
        gols.append(int(input(f"Gols na partida {i+1}: ")))

    jogador["gols"] = gols
    jogador["total"] = sum(gols)

    time.append(jogador)

    cont = input("Quer adicionar outro jogador? (S/N): ")
    if cont == "N":
        break

print("\nLista de jogadores:")
for i, j in enumerate(time):
    print(i, j["nome"])

while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar): "))

    if busca == 999:
        break

    if busca < len(time):
        print("Jogador:", time[busca]["nome"])
        print("Gols por partida:", time[busca]["gols"])
        print("Total:", time[busca]["total"])

'''