for cont_ex in range(1, 5):
    print(f"Rodada: {cont_ex}")
    # roda o print do 1 ao 4

    for cont_int in range(5, 0, -1):
        print(f"valor: {cont_int}")
        # roda o print de forma regresiva
        # do 5 ao 0 subtraindo -1 desse valor
print("fim")

# biblioteca que gera número aleatórios
import random

for A in range(1, 6):
    """o A vai rodar 5 vez tendo os valores
    1, 2, 3, 4, 5"""
    print(f"/Conjunto {A}")

    for B in range(5):
        # aqui vai repetir o B 5 vezes
        num = random.randint(1, 100)
        """ 
        depois salva um número aleatório entre 1 e 100 e exibe os números
        """
        print(f"valor: {num}")


for cartela in range(1, 6):
    numeros = random.sample(range(1, 61), 6)
    numeros.sort()
    print(f"Cartela {cartela}: {numeros}")
