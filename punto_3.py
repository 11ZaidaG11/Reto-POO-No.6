import random


def create_list() -> list: # Lista de numeros aleatorios de tamaño aleatorio
    list_random: list = []
    lon: int = random.randrange(5, 16)

    for _ in range(lon):
        list_random.append(random.randrange(1, 101))
    return list_random

def verification(list_random:list) -> list:
    list_prime: list = []

    for n in list_random:
        dividers = []
        for i in range(1, n+1): 
            if n % i == 0: # Dividir n con todos los numeros <= que el
                dividers.append(i)
        if len(dividers) == 2: # Si solo hay 2 divisores (1, n) es primo
            list_prime.append(i)          
    return list_prime

if __name__ == "__main__":
    cl = create_list()
    v = verification(cl)
    print(cl)
    if not v:
        print("Niniguno")
    else:
        print(v)