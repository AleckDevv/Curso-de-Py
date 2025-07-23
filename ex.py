# validador de senha
"""senha = ""

while senha != "admin123":
    senha = str(input("Digite a senha: "))
    if senha != "admin123":
        print("senha incorreta")
print("Acesso permitido")"""


# impar ou par
""" num = int(input("Digite um número: "))
if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"o número {num} é ímpar") """

# contagem de números
""" n = 0
while n < 10:
    n += 1
    print(n)
 """

# calculadora básica
""" num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
print(f"soma: {soma}")
print(f"subtracao: {subtracao}")
print(f"multiplicação: {multiplicacao}")
print(f"divisão: {divisao}") """

# área do triangulo
""" base = int(input("Digite a base"))
altura = int(input("Digite a altura"))

calculo = base * altura
print(f"a área é: {calculo}") """


# conversor de temperatura
""" graus_celsius = float(input("Digite a temperatura em C: "))

calculo = graus_celsius * 1.8 + 32
print(f"A temperatura em celsius: {graus_celsius} para F é: {calculo}") """


# comparador de números
""" n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n1 > n2:
    print(f"{n1}")
elif n2 > n1:
    print(f"{n2}") """

# verificar palavra
""" palavra = str(input("Digite uma palavra"))
if palavra == "Python":
    print("É igual")
else:
    print("não é igual") """


# login

""" usuario = ""
senha = 0

while usuario != "admin" or senha != 1234:
    usuario = str(input("Digiteo usuário: "))
    senha = int(input("Digite a senha: "))

    if usuario != "admin" or senha != 1234:
        print("Acesso negado. Tente novamente")
print("acesso permitido") """

# entrada cinema
""" idade = int(input("Digite a idade"))
carteira_estudante = bool(input("Tem carteira de estudante"))

if (idade < 18) and (carteira_estudante == True):
    print("Entrada gratuita")
elif (idade >= 18) and (carteira_estudante == False):
    print("Entrada Negada")
else:
    print("Apenas alunos") """

