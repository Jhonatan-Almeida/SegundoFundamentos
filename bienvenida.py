mensaje = "estas usando python"
print(mensaje)

nombre = input("Introduce tu nombre: ")

nombre = nombre.replace(".", "")

nombre = nombre.capitalize()

mensaje_mayus = mensaje.upper()
print(f"¡HOLA, {nombre.upper()}, {mensaje_mayus}!")

mensaje_minus = mensaje.lower()
print(f"¡hola, {nombre.lower()}, {mensaje_minus}!")

print(f"¡Hola, {nombre}, estas usando Python!")
