'''
===============================
EXERCÍCIO 1 - CONTAGEM REGRESSIVA (RECURSIVO)
===============================

import time

def contagem(n):

    if n == 0:
        print("FOGO!")
        return

    print(n)
    time.sleep(1)
    contagem(n - 1)


numero = int(input("Digite um número: "))
contagem(numero)

'''


'''
===============================
EXERCÍCIO 2 - FATORIAL RECURSIVO
===============================


def fatorial(n):

    if n == 0 or n == 1:
        return 1

    return n * fatorial(n - 1)


numero = int(input("Digite um número: "))
print("Fatorial:", fatorial(numero))

'''


'''
===============================
EXERCÍCIO 3 - FIBONACCI RECURSIVO
===============================


def fib(n):

    if n == 1 or n == 2:
        return 1

    return fib(n - 1) + fib(n - 2)


numero = int(input("Digite a posição da sequência: "))
print("Resultado:", fib(numero))

'''


'''
===============================
EXERCÍCIO 4 - SOMA DE LISTA (HEAD & TAIL)
===============================


def somar_lista(lista):

    if lista == []:
        return 0

    return lista[0] + somar_lista(lista[1:])


numeros = [1, 2, 3, 4, 5]

print("Lista:", numeros)
print("Soma:", somar_lista(numeros))

'''


'''
===============================
EXERCÍCIO 5 - POTENCIAÇÃO RECURSIVA
===============================


def potencia(base, expoente):

    if expoente == 0:
        return 1

    return base * potencia(base, expoente - 1)


base = int(input("Base: "))
expoente = int(input("Expoente: "))

print("Resultado:", potencia(base, expoente))

'''


'''
===============================
EXERCÍCIO 6 - INVERSÃO DE STRING
===============================


def inverter(texto):

    if texto == "":
        return ""

    return texto[-1] + inverter(texto[:-1])


palavra = input("Digite uma palavra: ")

print("Invertida:", inverter(palavra))

'''


'''
===============================
EXERCÍCIO 7 - TORRE DE HANOI
===============================


def hanoi(n, origem, destino, auxiliar):

    if n == 1:
        print(f"Mover disco 1 de {origem} para {destino}")
        return

    hanoi(n - 1, origem, auxiliar, destino)

    print(f"Mover disco {n} de {origem} para {destino}")

    hanoi(n - 1, auxiliar, destino, origem)


discos = int(input("Número de discos: "))

hanoi(discos, "A", "C", "B")

'''