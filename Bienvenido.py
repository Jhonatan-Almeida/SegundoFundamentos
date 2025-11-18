# Paso 1: Almacenar el mensaje en una variable
mensaje_base = "estas usando python"

# Paso 2: Pedir el nombre al usuario
nombre = input("Por favor, introduce tu nombre: ")

# Paso 6: Eliminar puntos en el nombre (si los hay)
nombre = nombre.replace('.', '')

# Paso 5: Formatear el nombre: primera letra mayúscula, resto minúsculas
nombre = nombre.capitalize()

# Paso 7: Crear el mensaje final con formato correcto
mensaje_final = f"¡Hola, {nombre}, {mensaje_base}!"

# Mostrar el mensaje
print(mensaje_final)

# Opcional: Otros formatos

# Paso 3: Todo en mayúsculas
# print(f"¡HOLA, {nombre.upper()}, {mensaje_base.upper()}!")

# Paso 4: Todo en minúsculas
# print(f"¡hola, {nombre.lower()}, {mensaje_base.lower()}!")
