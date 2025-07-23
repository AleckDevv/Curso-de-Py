lista = [1, 2, 3, 4]

for i in lista:
    print(i * 2)

palavra = "ascascsca"
for letra in palavra:
    print(letra)

nome = ["Alex Soares", "Maria Paz", "João Vitor"]

for primeiro in nome:
    primeiro_nome = primeiro.split(" ")[0]
    print(primeiro_nome)

elementos = [
    "elemento1",
    "elemento2",
    "elemento3",
    "elemento4",
    "elemento5",
    "elemento6",
]

for item in elementos:
    if item == "elemento4":
        continue
    print(item)
""" 
continue é um método que pula a próxima iteração do loop for mas o laço continua
até o final da execução
"""


