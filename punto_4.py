import random


def create_list() -> list: # Lista de numeros aleatorios de tamaño aleatorio
    list_random: list = []
    lon: int = random.randrange(5, 16)

    for _ in range(lon):
        list_random.append(random.randrange(1, 101))
    return list_random

def verification(list_random:list) -> int:
    candidates: list = []
    for i in range(len(list_random)-1): # -1 ya que se tiene i+1 
        add = list_random[i] + list_random[i+1]
        candidates.append(add)
    candidates.sort(reverse = True) # Ordena la lista
    result = candidates[:1]
    return result[0] # Imprimir como numero en vez de lista

if __name__ == "__main__":
    cl = create_list()
    v = verification(cl)
    print(cl)
    print(v)