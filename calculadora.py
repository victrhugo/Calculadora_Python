def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: Divisão por zero"

print("Selecione a operação:")
print("1. Soma")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite o número da operação desejada: ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if opcao == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif opcao == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif opcao == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif opcao == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Opção inválida")