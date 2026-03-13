#Exercício 5


#1. O Maior e o Menor
print("Exercício 1 - Maior e Menor")

lista = []

for i in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)

print("Lista completa:", lista)
print("Maior valor:", max(lista))
print("Menor valor:", min(lista))


#2. Pares e Ímpares
print("Exercício 2 - Pares e Ímpares")

numeros = []

while True:
    n = int(input("Digite um número: "))
    numeros.append(n)

    resp = input("Quer continuar? (S/N): ").upper()
    if resp == "N":
        break

pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("Lista completa:", numeros)
print("Pares:", pares)
print("Ímpares:", impares)


#3. Função de Área
print("Exercício 3 - Área do Terreno")

def area(largura, comprimento):
    resultado = largura * comprimento
    print("A área é", resultado, "m²")

l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))

area(l, c)


#4. Fatorial
print("Exercício 4 - Fatorial")

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

numero = int(input("Digite um número: "))
print("Fatorial:", fatorial(numero))


#5. Validação de Voto
print("Exercício 5 - Voto")

def voto(ano):
    idade = 2025 - ano

    if idade < 16:
        return "NEGADO"
    elif idade == 16 or idade == 17 or idade > 70:
        return "OPCIONAL"
    else:
        return "OBRIGATÓRIO"

ano = int(input("Digite seu ano de nascimento: "))
print("Situação do voto:", voto(ano))


#6. Matriz 3x3
print("Exercício 6 - Matriz")

matriz = []
soma = 0

for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f"Digite um valor para [{i},{j}]: "))
        linha.append(valor)
        soma = soma + valor
    matriz.append(linha)

print("Matriz:")

for linha in matriz:
    print(linha)

print("Soma dos valores:", soma)


# 7. Sistema de Notas
print("Exercício 7 - Sistema de Notas")

def notas(lista_notas):
    quantidade = len(lista_notas)
    maior = max(lista_notas)
    menor = min(lista_notas)
    media = sum(lista_notas) / quantidade

    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"

    resultado = {
        "Quantidade": quantidade,
        "Maior": maior,
        "Menor": menor,
        "Média": media,
        "Situação": situacao
    }

    return resultado


notas_aluno = []

qtd = int(input("Quantas notas deseja digitar? "))

for i in range(qtd):
    nota = float(input("Digite a nota: "))
    notas_aluno.append(nota)

print(notas(notas_aluno))