# --- Ejercicio 1: Pirámide de estrellas ---
print("=== PIRÁMIDE DE ESTRELLAS ===")

n = int(input("Ingresa un número entero (cantidad de estrellas del centro): "))

# Parte ascendente
for i in range(1, n + 1):
    print("*" * i)

# Parte descendente
for i in range(n - 1, 0, -1):
    print("*" * i)

# --- Ejercicio 2: Comprobación de contraseña ---
print("\n=== VERIFICACIÓN DE CONTRASEÑA ===")
print("La contraseña .\n")

password_correcta = "1995"
password_usuario = ""

# Repetir hasta que ingrese la contraseña correcta
while password_usuario != password_correcta:
    password_usuario = input("Introduce la contraseña: ")

print("Acceso concedido. Contraseña correcta.")

# --- Ejercicio 3: Mostrar palabra al revés ---
print("\n=== PALABRA AL REVÉS ===")

palabra = input("Introduce una palabra: ")

print("Letras desde la última hasta la primera:")
for letra in reversed(palabra):
    print(letra)

# --- Ejercicio 4: Contar letra en frase ---
print("\n=== CONTAR LETRA EN FRASE ===")

frase = input("Introduce una frase: ")
letra = input("Introduce una letra para contar cuántas veces aparece: ")

contador = 0

for caracter in frase:
    if caracter == letra:
        contador += 1

print(f"La letra '{letra}' aparece {contador} veces en la frase.")


