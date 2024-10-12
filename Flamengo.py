# Função para adicionar
def add(x, y):
    return x + y

# Função para subtrair
def subtract(x, y):
    return x - y

# Função para multiplicar
def multiply(x, y):
    return x * y

# Função para dividir
def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

print("Selecione a operação:")
print("1.Adicionar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")

while True:
    # Receber a entrada do usuário
    escolha = input("Digite a escolha (1/2/3/4): ")

    # Verificar se a escolha é uma das opções
    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif escolha == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif escolha == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif escolha == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # Perguntar ao usuário se deseja realizar outra operação
        repetir = input("Quer realizar outra operação? (sim/não): ")
        if repetir.lower() != 'sim':
            break
    else:
        print("Escolha inválida!")
