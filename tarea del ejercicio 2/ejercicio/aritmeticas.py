# Autor: Wendy
# Ejercicio A: Operación aritmética

print("=== EJERCICIO A ===")
# Operación: ((3 + 2) / (2 * 5))^2

resultado = ((3 + 2) / (2 * 5)) ** 2

print("El resultado de la operación es:", resultado)

# Autor: Wendy
# Ejercicio B: Fórmula n(n+1)/2

print("=== EJERCICIO B ===")

n = int(input("Ingresa un número entero positivo: "))

resultado = n * (n + 1) / 2

print("El resultado de la operación es:", resultado)

# Autor: Wendy
# Ejercicio C: Cociente y resto

print("=== EJERCICIO C ===")

num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

cociente = num1 // num2   # División entera
resto = num1 % num2       # Resto de la división

print("\nPrimer número ingresado:", num1)
print("Segundo número ingresado:", num2)
print("Cociente:", cociente)
print("Resto:", resto)
