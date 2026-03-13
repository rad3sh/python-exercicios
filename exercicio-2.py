#Exercício 2

#1. Antecessor e Sucessor
numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

print("O antecessor é", antecessor, "e o sucessor é", sucessor)


#2. Calculadora de Média
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("A média é:", round(media, 1))


#3. Dobro, Triplo e Raiz
num = float(input("Digite um número: "))

dobro = num * 2
triplo = num * 3
raiz = num ** 0.5

print("Dobro:", dobro)
print("Triplo:", triplo)
print("Raiz quadrada:", raiz)


#4. Divisão de balas
balas = 50
criancas = 6

cada = balas // criancas
sobra = balas % criancas

print("Cada criança recebe:", cada)
print("Balas que sobram:", sobra)


#5. Conversor de moeda
dolar = 5.80

reais = float(input("Digite quanto dinheiro você tem em reais: "))

dolares = reais / dolar

print("Você pode comprar", format(dolares, ".2f"), "dólares")


#6. Validação de acesso
idade = int(input("Digite sua idade: "))
convite = input("Você possui convite? (True ou False): ")

if idade > 18 and convite == "True":
    print(True)
else:
    print(False)


#7. Desconto de produto
preco = float(input("Digite o preço do produto: "))

novo_preco = preco - (preco * 15 / 100)

print("O novo preço com desconto é:", novo_preco)

#------------------------------------------------------------------------------