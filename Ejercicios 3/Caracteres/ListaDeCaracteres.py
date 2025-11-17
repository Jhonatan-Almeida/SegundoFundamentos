# 1
frutas = ["manzana", "plátano", "cereza", "pera", "higo", "frambuesa", "fresa"]
print("1 – Lista creada:", frutas)

# 2
print("2 – Longitud:", len(frutas))

# 3
print("3 – Índice 3:", frutas[3])

# 4
frutas[1] = "mora"
print("4 – Modificado índice 1:", frutas)

# 5
frutas.append("mango")
print("5 – Añadido mango:", frutas)

# 6
frutas.insert(0, "uva")
print("6 – Insertada uva al principio:", frutas)

# 7
print("7 – Bucle simple:")
for f in frutas:
    print("  ", f)

# 8
ultima_fruta = frutas.pop()
print("8 – Última fruta extraída:", ultima_fruta)

# 9
print("9 – Lista tras pop:")
for f in frutas:
    print("  ", f)

# 10
print("10 – Fruta y su longitud:")
for f in frutas:
    print(f"   {f} -> {len(f)}")

# 11
print("11 – Solo nombres con más de 5 caracteres:")
for f in frutas:
    if len(f) > 5:
        print("  ", f)

# 12
frutas.remove("cereza")
print("12 – Tras eliminar cereza:", frutas)

# 13
frutas.clear()
print("13 – Lista vacía:", frutas)