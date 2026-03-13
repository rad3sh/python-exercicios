#Exercício 4

from random import randint

#1. Contagem de Pares
print("Exercício 1 - Números pares de 1 a 50")

for i in range(1, 51):
    if i % 2 == 0:
        print(i)


#2. Soma dos Pares
print("Exercício 2 - Soma dos números pares")

soma = 0

for i in range(6):
    num = int(input("Digite um número: "))
    
    if num % 2 == 0:
        soma = soma + num

print("A soma dos números pares é:", soma)


#3. Jogo da Adivinhação
print("Exercício 3 - Jogo de Adivinhação")

numero_secreto = randint(0, 10)
tentativas = 0
acertou = False

while not acertou:
    chute = int(input("Tente adivinhar o número (0 a 10): "))
    tentativas = tentativas + 1

    if chute == numero_secreto:
        acertou = True
    elif chute < numero_secreto:
        print("Mais alto...")
    else:
        print("Mais baixo...")

print("Você acertou!")
print("Tentativas:", tentativas)


#4. Tratamento de Dados
print("Exercício 4 - Digite números (999 para parar)")

soma = 0
contador = 0

while True:
    num = int(input("Digite um número: "))

    if num == 999:
        break

    soma = soma + num
    contador = contador + 1

print("Quantidade de números digitados:", contador)
print("Soma dos números:", soma)


#5. Tabuada Personalizada
print("Exercício 5 - Tabuada")

while True:
    numero = int(input("Digite um número para ver a tabuada (negativo para sair): "))

    if numero < 0:
        break

    for i in range(1, 11):
        print(numero, "x", i, "=", numero * i)


#6. Detector de Palíndromo
print("Exercício 6 - Palíndromo")

frase = input("Digite uma frase: ")

frase = frase.replace(" ", "").lower()
invertida = frase[::-1]

if frase == invertida:
    print("É um palíndromo")
else:
    print("Não é um palíndromo")


# 7. Análise de Grupo
print("Exercício 7 - Análise de pessoas")

maior18 = 0
homens = 0
mulheres_menos20 = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()

    if idade > 18:
        maior18 = maior18 + 1

    if sexo == "M":
        homens = homens + 1

    if sexo == "F" and idade < 20:
        mulheres_menos20 = mulheres_menos20 + 1

    continuar = input("Quer continuar? (S/N): ").upper()

    if continuar == "N":
        break

print("Pessoas com mais de 18 anos:", maior18)
print("Homens cadastrados:", homens)
print("Mulheres com menos de 20 anos:", mulheres_menos20)

#------------------------------------------------------------------------------
