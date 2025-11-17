# 1 listas
numeros = list(range(1, 11))
print("1 – Lista original:", numeros)

# 2 orden inverso
pares_inv = [n for n in numeros if n % 2 == 0][::-1]
print("2 – Pares en orden inverso:", pares_inv)

# 3 cuadrados
print("3 – Cuadrados:")
for n in numeros:
    print(n ** 2)

# 4  una línea cada uno
pares_inv_1line = [n for n in range(10, 0, -1) if n % 2 == 0]   # equivalente
cuadrados_1line = [n * n for n in numeros]
print("4 – Pares inv (1 línea):", pares_inv_1line)
print("   Cuadrados (1 línea):", cuadrados_1line)

# 5 mínimo
print("5 – Mínimo:", min(numeros))

# 6 máximo
print("6 – Máximo:", max(numeros))

# 7 con bucle
suma_bucle = 0
for n in numeros:
    suma_bucle += n
print("7 – Suma con bucle:", suma_bucle)
# sin bucle
print("   Suma sin bucle (sum):", sum(numeros))


print("8 – Índice del 8 en original:", numeros.index(8))
print("   Índice del 8 en pares_inv:", pares_inv.index(8) if 8 in pares_inv else "no está")