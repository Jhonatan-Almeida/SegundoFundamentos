# 1. Lista de frutas
frutas = ["manzana", "plátano", "cereza", "pera", "higo", "frambuesa", "fresa"]

# 2. Longitud de la lista
print("Longitud:", len(frutas))

# 3. Acceder al elemento 3
print("Elemento 3:", frutas[2])

# 4. Modificar segundo objeto a 'mora'
frutas[1] = "mora"

# 5. Añadir mango al final
frutas.append("mango")

# 6. Insertar uva al inicio
frutas.insert(0, "uva")

# 7. Recorrer la lista e imprimir
for f in frutas:
    print(f)

# 8. Eliminar último elemento y guardarlo
ultima_fruta = frutas.pop()
print("Última fruta:", ultima_fruta)

# 9. Recorrer lista
for f in frutas:
    print(f)

# 10. Imprimir longitud de cada fruta
for f in frutas:
    print(f, len(f))

# 11. Solo nombres con más de 5 caracteres
for f in frutas:
    if len(f) > 5:
        print(f)

# 12. Borrar 'cereza'
frutas.remove("cereza")

# 13. Vaciar la lista
frutas.clear()
print(frutas)
