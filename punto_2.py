import random


def create_list() -> list:
    # Lista de palindromos
    palin = [
        "reconocer", "sometemos", "acurruca", "arañara", "arenera", "arepera", "Neuquen", 
        "narran", "rallar", "radar", "rajar", "rapar", "sacas", "sagas", "salas", "sanas", 
        "seres", "somos", "anana", "alla", "aja", "ala", "ana", "ama", "ara", "asa", "ata",
        "aya", "eje","ese", "oro", "oso", "ojo", "alla"
        ]

    # Lista de palabras normales
    words = [
        "luz", "montaña", "cósmico", "rio", "teclado", "ventana", "nube", "dragon", 
        "camino", "planeta", "cristal", "misterio", "trueno", "jardin", "eco",
        "laberinto", "sol", "tinta", "bosque", "arena", "puerta", "universo", "piedra",
        "sombra", "aurora", "mariposa", "tormenta", "espejo", "aliento", "latido", 
        "llama", "fuego", "brisa", "espiral", "horizonte", "reflejo", "claridad", "ceniza", 
        "murmullo", "truco", "fantasma", "sabiduria", "chispa", "destino", "caverna",
        "silencio", "grieta", "encanto", "acantilado", "vertigo"
        ]
    
    cut: int = random.randrange(10, 16)
    join = palin + words
    final = random.sample(join, k = len(join)) # Desordena la lista
    final = final[:cut] # Toma entre 10 y 15 palabras para la lista final
    return final

def verification(final:list) -> list:
    yes_palin: list = []

    for word in final:
        for c in range(len(word) // 2): # Detenerse en la mitad de la palabra
            if word[c] == word[-(c+1)]: # Compara la primera letra con la ultima
                yes_palin.append(word)
            else:
                pass
    return yes_palin

if __name__ == "__main__":
    cl = create_list()
    v = verification(cl)
    print(cl)
    print(v)