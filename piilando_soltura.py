# ======================================
# PILLANDO SOLTURA - MENÚ INTERACTIVO
# ======================================

# 1. Elementos duplicados
def elementos_duplicados():
    lista = [1, 2, 3, 2, 4, 5, 1, 6]
    duplicados = []
    unicos = []
    for x in lista:
        if lista.count(x) > 1 and x not in duplicados:
            duplicados.append(x)
    for x in lista:
        if x not in duplicados:
            unicos.append(x)
    print("Duplicados:", duplicados)
    print("Solo únicos:", unicos)

# 2. Unir y ordenar listas
def unir_y_ordenar():
    lista1 = [3, 1, 4]
    lista2 = [2, 5, 0]
    union = sorted(lista1 + lista2)
    print("Listas unidas y ordenadas:", union)

# 3. Segundo número más grande
def segundo_mas_grande():
    lista = [5, 1, 9, 3, 7]
    segundo = sorted(set(lista))[-2]
    print("Segundo número más grande:", segundo)

# 4. Contar elementos mayores que un número
def contar_mayores():
    lista = [1, 5, 7, 9, 2]
    num = int(input("Introduce un número: "))
    count = sum(1 for x in lista if x > num)
    print("Cantidad de elementos mayores:", count)

# 5. Suma de números divisibles por n
def suma_divisibles():
    lista = [2, 3, 4, 5, 6, 12]
    n = int(input("Introduce un número: "))
    suma = sum(x for x in lista if x % n == 0)
    print(f"Suma de elementos divisibles por {n}: {suma}")

# 6. Número más alto inferior a un límite
def mayor_inferior():
    lista = [2, 5, 7, 10, 12]
    limite = int(input("Introduce un número límite: "))
    menores = [x for x in lista if x < limite]
    if menores:
        print("Número más alto inferior al límite:", max(menores))
    else:
        print("No hay números menores que el límite.")

# 7. Elementos comunes entre dos listas
def elementos_comunes():
    l1 = [1, 2, 3, 4]
    l2 = [3, 4, 5, 6]
    comunes = [x for x in l1 if x in l2]
    print("Elementos comunes:", comunes)

# 8. Contar apariciones de un elemento
def contar_apariciones():
    lista = [23, 65, 23, 23, 5]
    x = int(input("Introduce un número para contar sus apariciones: "))
    print(f"{x} aparece {lista.count(x)} veces.")

# 9. Lista solo con positivos
def solo_positivos():
    lista = [-1, 2, -3, 4, 5]
    positivos = [x for x in lista if x > 0]
    print("Números positivos:", positivos)

# 10. Tamaño de strings en una lista
def tamanos_strings():
    strings = ["hola", "mundo", "python"]
    tamanos = [len(s) for s in strings]
    print("Tamaño de cada string:", tamanos)

# 11. Strings en mayúscula
def strings_mayuscula():
    strings = ["hola", "mundo", "python"]
    mayusculas = [s.upper() for s in strings]
    print("Strings en mayúscula:", mayusculas)

# ======================================
# Menú interactivo
# ======================================
def menu():
    while True:
        print("\n=== PILLANDO SOLTURA - MENÚ ===")
        print("1. Elementos duplicados")
        print("2. Unir y ordenar listas")
        print("3. Segundo número más grande")
        print("4. Contar elementos mayores que un número")
        print("5. Suma de números divisibles por n")
        print("6. Número más alto inferior a un límite")
        print("7. Elementos comunes entre dos listas")
        print("8. Contar apariciones de un elemento")
        print("9. Lista solo con positivos")
        print("10. Tamaño de strings en una lista")
        print("11. Strings en mayúscula")
        print("12. Salir")
        opcion = input("Elige una opción (1-12): ")

        if opcion == "1":
            elementos_duplicados()
        elif opcion == "2":
            unir_y_ordenar()
        elif opcion == "3":
            segundo_mas_grande()
        elif opcion == "4":
            contar_mayores()
        elif opcion == "5":
            suma_divisibles()
        elif opcion == "6":
            mayor_inferior()
        elif opcion == "7":
            elementos_comunes()
        elif opcion == "8":
            contar_apariciones()
        elif opcion == "9":
            solo_positivos()
        elif opcion == "10":
            tamanos_strings()
        elif opcion == "11":
            strings_mayuscula()
        elif opcion == "12":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

# Ejecutar menú
menu()
