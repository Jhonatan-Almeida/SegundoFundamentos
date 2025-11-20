# Funciones

def piramides_de_estrellas():
    n = int(input("Introduce un número entero: "))
    for i in range(1, n+1):
        print("*" * i)
    for i in range(n-1, 0, -1):
        print("*" * i)

def contrasena():
    contraseña = "contraseña"
    entrada = ""
    while entrada != contraseña:
        entrada = input("Introduce la contraseña: ")
    print("¡Contraseña correcta!")

def letras_alrevez():
    palabra = input("Introduce una palabra: ")
    for letra in palabra[::-1]:
        print(letra)

def contar_letras():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")
    print(f"La letra '{letra}' aparece {frase.count(letra)} veces")


# Menú interactivo
def menu():
    while True:
        print("\n=== MENÚ DE EJERCICIOS ===")
        print("1. Pirámides de estrellas")
        print("2. Contraseña")
        print("3. Letras al revés")
        print("4. Contar letras")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")

        if opcion == "1":
            piramides_de_estrellas()
        elif opcion == "2":
            contrasena()
        elif opcion == "3":
            letras_alrevez()
        elif opcion == "4":
            contar_letras()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


# Ejecutar menú
menu()
