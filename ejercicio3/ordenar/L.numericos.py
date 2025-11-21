# --- 1. Crear la lista de números ---
numeros = [1,2,3,4,5,6,7,8,9,10]
print("Lista original:", numeros)

# --- 2. Crear una lista con los números pares en orden inverso ---
pares_inverso = []
for num in numeros:
    if num % 2 == 0:
        pares_inverso.append(num)
pares_inverso.reverse()
print("Pares en orden inverso:", pares_inverso)

# --- 3. Imprimir el cuadrado de cada número usando un bucle ---
print("\nCuadrado de cada número:")
for numero in numeros:
    print(numero**2)

# --- 4. Rehacer pasos 2 y 3 usando comprensiones de lista ---
pares_inverso_comp = [n for n in numeros if n % 2 == 0][::-1]
print("\nPares invertidos (comprensión):", pares_inverso_comp)

cuadrados_comp = [n**2 for n in numeros]
print("Cuadrados (comprensión):", cuadrados_comp)

# --- 5. Número más pequeño de la lista ---
minimo = min(numeros)
print("\nNúmero más pequeño:", minimo)

# --- 6. Número más alto de la lista ---
maximo = max(numeros)
print("Número más alto:", maximo)

# --- 7. Suma de todos los elementos (con y sin bucle) ---
suma_bucle = 0
for n in numeros:
    suma_bucle += n
print("\nSuma con bucle:", suma_bucle)

suma_funcion = sum(numeros)
print("Suma con sum():", suma_funcion)

# --- 8. Índice del número 8 en la lista original y en la lista de pares invertidos ---
indice_original = numeros.index(8)
print("\nÍndice de 8 en la lista original:", indice_original)

if 8 in pares_inverso:
    indice_pares = pares_inverso.index(8)
    print("Índice de 8 en la lista de pares invertidos:", indice_pares)
else:
    print("El número 8 no está en la lista de pares invertidos.")
