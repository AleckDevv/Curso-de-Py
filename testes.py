nome = "Alex"
print(f"nome: {nome}")
print(type(nome))

array = [10, "Alex", True, [10, 20, 30]]
print(array[3][0])
""" 
acesso ao array igual ao js
"""

objeto = {"nome": "Alex", "idade": 25}
print(objeto["nome"])


idade = 60
if idade <= 12:
    print("é uma criança")
elif (idade >= 18) and (idade <= 59):
    print("é um adulto")
else:
    print("é um idoso")
