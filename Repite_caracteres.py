
texto = input("Introduce un string de 5 caracteres: ")


if len(texto) != 5:
    print("Debes introducir exactamente 5 caracteres.")
else:
    resultado = ""
    for c in texto:
        resultado += c*2 
    print("Resultado:", resultado)
