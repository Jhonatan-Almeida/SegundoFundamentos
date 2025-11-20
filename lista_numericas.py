numeros = [1,2,3,4,5,6,7,8,9,10]

# 2. Números pares en orden inverso
pares_invertidos = [x for x in numeros if x%2==0][::-1]
print(pares_invertidos)

# 3. Cuadrado de cada número
for x in numeros:
    print(x**2)

# 4. Versión comprimiendo todo
cuadrados = [x**2 for x in numeros]
print(cuadrados)

# 5. Número más pequeño
print("Mínimo:", min(numeros))

# 6. Número más grande
print("Máximo:", max(numeros))

# 7. Suma con y sin bucle
suma1 = sum(numeros)
suma2 = 0
for x in numeros:
    suma2 += x
print(suma1, suma2)

# 8. Índice del número 8
print("Índice 8 en original:", numeros.index(8))
print("Índice 8 en pares invertidos:", pares_invertidos.index(8) if 8 in pares_invertidos else "No está")
