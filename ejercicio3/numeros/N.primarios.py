# --- NÚMEROS PRIMOS ENTRE 2 Y 100 ---

print("=== NÚMEROS PRIMOS ENTRE 2 Y 100 ===")

# Recorremos todos los números desde 2 hasta 100
for numero in range(2, 101):

    es_primo = True  # Suponemos que el número ES primo

    # Comprobamos si tiene algún divisor
    for divisor in range(2, numero):
        if numero % divisor == 0:   # Si tiene divisor distinto de 1 y sí mismo
            es_primo = False
            break  # Ya no es primo, salimos del bucle

    # Si sigue siendo primo, lo imprimimos
    if es_primo:
        print(numero)

