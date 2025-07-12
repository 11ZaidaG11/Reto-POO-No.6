def convertion():
    all_ascii: list = []
    word_ascii: list = [] 
    for word in user:
        ascii: list = [] 
        for c in word: # ASCII de cada palabra
            ascii.append(ord(c))
        ascii.sort() # Orden ascendente
        all_ascii.append(ascii)
        word_ascii.append([word, ascii]) # Lista par palabra, ASCII
    return all_ascii, word_ascii

def verification(all_ascii:list) -> list:
    equal: list = []
    for i in range(len(all_ascii)):
        for j in range(i+1, len(all_ascii)): # Dos indices para comparar dos elementos
            if all_ascii[i] not in equal: # Para evitar repeticiones
                if all_ascii[i] == all_ascii[j]:
                    equal.append(all_ascii[i])
                else:
                    pass
    return equal

def asignation(word_ascii:list, equal:list) -> list: # Si el ASCII esta en equal agregar la palabra
    result: list = []
    for w, n in word_ascii: 
        if n in equal:
            result.append(w)
    return result


if __name__ == "__main__":
    user: str = input("Ingrese las palabras separadas por comas: ")
    user = user.split(",")
    a, w_a = convertion()
    v = verification(a)
    asi = asignation(w_a, v)
    if asi:
        print("Los anagramas son:")
        print(", ".join(asi)) # Para imprimir la lista como texto
    else:
        print("No se encontraron anagramas")