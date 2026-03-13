#1. Identificação de Tipos

numero_inteiro = 2
numero_float = 3.1
texto = "Olá"
verdadeiro = True

print(f"O tipo da variavel {numero_inteiro} é: {type(numero_inteiro)}")
print(f"O tipo da variavel {numero_float} é: {type(numero_float)}")
print(f"O tipo da variavel {texto} é: {type(texto)}")
print(f"O tipo da variavel {verdadeiro} é: {type(verdadeiro)}")


#2. O "Bug" da Concatenação (Casting)

idade = 28
print("Eu tenho " + str(idade) + " anos.")


#3. Soma de Inputs (Cuidado com Strings)

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

soma = int(num1) + int(num2)

print("A soma é:", soma)


#4. Conversão de Float para Int

numero = 15.89
numero_inteiro = int(numero)

print("Número convertido:", numero_inteiro)


#5. O Poder do Booleano

x = 10
y = 5

resultado = x > y

print("Resultado:", resultado)
print("Tipo:", type(resultado))


#6. Informações do Usuário (Formatação)

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
altura = input("Digite sua altura: ")

print(f"Olá {nome}, você tem {idade} anos e mede {altura} metros.")


#7. Tipos dentro de Strings

numero_texto = "50"
resultado1 = int(numero_texto) * 2
resultado2 = float(numero_texto) * 2
resultado3 = numero_texto * 2

print("Inteiro * 2 =", resultado1)
print("Float * 2 =", resultado2)
print("String * 2 =", resultado3)

#------------------------------------------------------------------------------