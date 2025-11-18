## 📝 Script de Manipulación de Diccionarios (Clave: Fruta, Valor: Stock)

# 1. Crea un diccionario llamado productos con las frutas y su stock inicial.
print("--- 1. Creando el diccionario inicial ---")
productos = {
    "manzana": 150,
    "plátano": 200,
    "cereza": 80,
    "pera": 120,
    "higo": 50,
    "frambuesa": 95,
    "fresa": 180
}
print(f"Diccionario inicial: {productos}")

# 2. Usa la función len() para imprimir el número de pares clave-valor (longitud) del diccionario.
print("\n--- 2. Longitud (número de pares clave-valor) ---")
longitud_productos = len(productos)
print(f"El diccionario contiene {longitud_productos} productos.")

# 3. Accede al stock del producto "pera" (similar a acceder al objeto 3 en la lista).
print("\n--- 3. Accediendo al stock de 'pera' ---")
# Usamos el nombre de la fruta como clave para acceder a su valor.
stock_pera = productos["pera"]
print(f"El stock actual de peras es: {stock_pera}")

# 4. Modifica el stock del producto "plátano" (similar a modificar el segundo objeto de la lista), cambiando su stock a 300.
print("\n--- 4. Modificando el stock de 'plátano' a 300 ---")
productos["plátano"] = 300
print(f"Nuevo stock de plátano: {productos['plátano']}")
print(f"Diccionario después de la modificación: {productos}")

# 5. Añade el nuevo par clave-valor "mango" con stock 100 al final del diccionario.
print("\n--- 5. Añadiendo 'mango' al diccionario ---")
# En diccionarios, agregar es simplemente asignar un valor a una nueva clave.
productos["mango"] = 100
print(f"Diccionario después de añadir 'mango': {productos}")

# 6. Insertar "uva" al comienzo: Los diccionarios no tienen un orden garantizado
#    en Python hasta la versión 3.7+ (aunque en 3.7+ sí mantienen el orden de inserción).
#    Simplemente lo añadiremos:
print("\n--- 6. Insertando 'uva' (añadiendo un nuevo par clave-valor) ---")
productos["uva"] = 75
print(f"Diccionario después de añadir 'uva': {productos}")

# 7. Usa un bucle para recorrer las claves (nombres de frutas) e imprimir cada una por la consola.
print("\n--- 7. Recorriendo e imprimiendo solo las claves (frutas) ---")
for fruta in productos:
    print(f"Clave (Fruta): {fruta}")

# 8. Usa el método .pop() para eliminar el último par clave-valor ("mango") y guárdalo en una variable.
# NOTA: En diccionarios modernos de Python, .popitem() elimina el último elemento insertado (en este caso, 'uva' o 'mango',
# dependiendo de la versión y el orden interno). Usaremos .pop() con una clave específica.
print("\n--- 8. Eliminando la fruta 'fresa' y guardando su stock ---")
try:
    stock_fresa_eliminada = productos.pop("fresa")
    print(f"Stock eliminado de 'fresa': {stock_fresa_eliminada}")
    print(f"Diccionario después de pop('fresa'): {productos}")
except KeyError:
    print("La clave 'fresa' no existe en el diccionario.")

# 9. Realiza un bucle que recorra el diccionario e imprima cada par clave-valor (fruta y stock).
print("\n--- 9. Recorriendo e imprimiendo pares clave:valor ---")
for fruta, stock in productos.items():
    print(f"La fruta '{fruta}' tiene un stock de {stock} unidades.")

# 10. Modifica el script para que imprima también la longitud de cada nombre de fruta (clave).
print("\n--- 10. Imprimiendo clave, valor y longitud de la clave ---")
for fruta, stock in productos.items():
    longitud_nombre = len(fruta)
    print(f"Fruta: {fruta} ({longitud_nombre} caracteres) | Stock: {stock}")

# 11. Modifica el script para que recorra el diccionario e imprima solo aquellos
#     nombres (claves) que tengan más de 5 caracteres.
print("\n--- 11. Imprimiendo claves con MÁS de 5 caracteres ---")
for fruta in productos.keys(): # Recorremos solo las claves
    if len(fruta) > 5:
        print(f"-> Clave con más de 5 caracteres: {fruta}")

# 12. Usa el método .pop() para borrar el par clave-valor de "cereza" del diccionario.
print("\n--- 12. Eliminando el par 'cereza' con .pop('cereza') ---")
try:
    productos.pop("cereza")
    print(f"Diccionario después de pop('cereza'): {productos}")
except KeyError:
    print("La clave 'cereza' ya fue eliminada.")

# 13. Usa el método clear() para vaciar el diccionario.
print("\n--- 13. Vaciando el diccionario con .clear() ---")
productos.clear()
print(f"Diccionario después de clear(): {productos}")
print(f"Longitud final: {len(productos)}")