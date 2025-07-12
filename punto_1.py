def operation(num_a:int, num_b:int, sign:str):
    match sign:
        case "+": # Suma
            result = num_a + num_b
        case "-": # Resta
            result = num_a - num_b
        case "*": # Multiplicacion
            result = num_a * num_b
        case "/": # Division
            result = num_a / num_b
        case _:
            result = "Opción no disponible"
    return result
    
if __name__ == "__main__":
    num_a = int(input("Ingrese un numero: "))
    num_b = int(input("Ingrese otro numero: "))
    print("Ingrese:\n+ para suma\n" \
    "- para resta\n" \
    "* para multiplicación\n" \
    "/ para división")
    sign: str = input("→ ")

    res = operation(num_a, num_b, sign)
    print(f"{num_a} {sign} {num_b} = {res}")