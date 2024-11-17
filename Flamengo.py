import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

def power(x, y):
    return x ** y

def sine(x):
    return math.sin(x)

def cosine(x):
    return math.cos(x)

def tangent(x):
    return math.tan(x)

def get_choice():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide,
        '5': power,
        '6': sine,
        '7': cosine,
        '8': tangent
    }
    while True:
        try:
            choice = input("Digite a escolha: ")
            if choice in operations:
                return operations[choice]
            else:
                print("Escolha inválida!")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

def get_numbers():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

while True:
    operation = get_choice()
    num1, num2 = get_numbers()

    try:
        result = operation(num1, num2)
        print(f"{num1} {operation.__name__} {num2} = {result}")
    except TypeError:
        print("Essa operação requer dois números.")

    repeat = input("Quer realizar outra operação? (sim/não): ")
    if repeat.lower() != 'sim':
        break
