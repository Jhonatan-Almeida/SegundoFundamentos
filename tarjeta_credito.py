
tarjeta = input("Introduce el número de la tarjeta de crédito: ")


tarjeta_sin_espacios = tarjeta.replace(" ", "")


ultimos4 = tarjeta_sin_espacios[-4:]


cantidad_ocultos = len(tarjeta_sin_espacios) - 4
ocultos = "*" * cantidad_ocultos


resultado = ""

for i, char in enumerate(ocultos + ultimos4):
    if i % 4 == 0 and i != 0:
        resultado += " "
    resultado += char

print("Tarjeta enmascarada:")
print(resultado)
