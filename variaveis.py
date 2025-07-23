# variáveis e tipos de dados
nome = "Alex"
idade = 25
verdadeiro = True
falso = False
flutuante = 1.2
array = [10, "teste", True]
objeto = {nome: "Alex", idade: 25}

print(type(nome))
""" 
função type() para saber o tipo de dados
 """
print(array)

""" 
isinstance() verifica se determinada veriável
é de tal tipo de dados
 """
print(isinstance(idade, int))
print(isinstance(nome, int))
""" 
tem como verificar mais de um tipo em uma condição
 """
print(isinstance(idade, (int, float)))


nome2 = "Alex Soares"
idade2 = 18
altura = 1.75
tem_carteira = True

""" 
template string em py
 """
print(f"tetse: {nome2}")

# str
nome3 = "pedro"

# int
ano = 2025

# float
preco = 9.99

# booleano
tem_carteira = True
esta_chovendo = False

# array
cidades = ["São Paulo", "Rio", "Belo Horizonte", 10, True]

# objeto
usuario = {
    "nome": "Alex",
    "idade": 24,
    "email": "alex@gmail.com"
}

# none
vazio = None