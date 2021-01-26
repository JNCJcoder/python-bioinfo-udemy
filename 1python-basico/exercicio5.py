num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operador = input("Digite o operador numero: ")

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "/":
    resultado = num1 / num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "%":
    resultado = num1 % num2
else:
    print("Operador Invalido")

print("o resultado e: ", resultado)