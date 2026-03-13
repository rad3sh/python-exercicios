#Exercício 3

#1. Radar de Velocidade
print("Exercício 1 - Radar de Velocidade")

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade > 80:
    print("Você foi multado!")
else:
    print("Boa viagem!")


#2. Par ou Ímpar
print("Exercício 2 - Par ou Ímpar")

numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é PAR")
else:
    print("O número é ÍMPAR")


#3. O Maior Número
print("Exercício 3 - Maior Número")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

if n1 > n2:
    print("O primeiro valor é maior")
elif n2 > n1:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")


#4. Cálculo da Bilheteira
print("Exercício 4 - Preço da Viagem")

distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print("O preço da viagem é:", preco)


#5. Classificação de Idade
print("Exercício 5 - Classificação de Idade")

ano_nascimento = int(input("Digite o ano de nascimento: "))
idade = 2025 - ano_nascimento

if idade <= 12:
    print("Classificação: Criança")
elif idade <= 17:
    print("Classificação: Adolescente")
elif idade <= 64:
    print("Classificação: Adulto")
else:
    print("Classificação: Sênior")


#6. Simulador de Empréstimo
print("Exercício 6 - Empréstimo Bancário")

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite seu salário: "))
anos = int(input("Em quantos anos você vai pagar? "))

meses = anos * 12
prestacao = valor_casa / meses
limite = salario * 0.30

print("Prestação mensal:", prestacao)

if prestacao > limite:
    print("Empréstimo NEGADO")
else:
    print("Empréstimo APROVADO")


#7. Mini Calculadora
print("Exercício 7 - Mini Calculadora")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print("Resultado:", resultado)

elif operacao == "-":
    resultado = num1 - num2
    print("Resultado:", resultado)

elif operacao == "*":
    resultado = num1 * num2
    print("Resultado:", resultado)

elif operacao == "/":
    resultado = num1 / num2
    print("Resultado:", resultado)

else:
    print("Operação inválida!")

#------------------------------------------------------------------------------