

def piramide():
    n = int(input("Número de estrellas en el centro: "))
    for i in range(1, n + 1): print("*" * i)
    for i in range(n - 1, 0, -1): print("*" * i)

def password():
    while input("Contraseña: ") != "contraseña":
        print("Incorrecta.")
    print("Correcta.")

def reversa():
    for c in input("Palabra: ")[::-1]: print(c)

def contar_letra():
    f, l = input("Frase: "), input("Letra a contar: ")
    print(f.lower().count(l.lower()))

if __name__ == "__main__":
    opciones = {1: piramide, 2: password, 3: reversa, 4: contar_letra}
    while True:
        print("\n1-Pirámide  2-Password  3-Reversa  4-Contar letra  0-Salir")
        try:
            op = int(input(">> "))
            if op == 0:
                break
            opciones[op]()
        except (ValueError, KeyError):
            print("Opción inválida.")