"""
=== EJERCICIO DE BIENVENIDA
"""

print("=== EJERCICIO DE BIENVENIDA ===")


mensaje = 'estas usando python'
print(f"\n1. Mensaje en variable: {mensaje}")


nombre_usuario = input("\n2. Por favor, introduce tu nombre: ")


nombre_formateado = nombre_usuario.capitalize()
print(f"   Nombre formateado: {nombre_formateado}")


nombre_formateado = nombre_formateado.replace('.', '')
print(f"   Nombre sin puntos: {nombre_formateado}")


print("\n--- RESULTADOS FINALES ---")


print(f"a) ¡Hola, {nombre_formateado}, {mensaje}!")

# MAYÚSCULAS
print(f"b) ¡HOLA, {nombre_formateado.upper()}, {mensaje.upper()}!")

# minúsculas
print(f"c) ¡hola, {nombre_formateado.lower()}, {mensaje.lower()}!")

# formato correcto
mensaje_final = mensaje.replace('python', 'Python')
print(f"d) ¡Hola, {nombre_formateado}, {mensaje_final}!")

print("\n¡Ejercicio completado!")