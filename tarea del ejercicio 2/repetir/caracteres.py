# Script para duplicar caracteres de un string de 5 letras
# Autor: Wendy

print("=== DUPLICAR CARACTERES ===")

# Leer el string
texto = input("Ingresa un string de 5 caracteres: ")

# Validar que tenga exactamente 5 caracteres
if len(texto) != 5:
    print("Error: Debe contener exactamente 5 caracteres.")
else:
    # Duplicar cada carácter
    resultado = ""
    for caracter in texto:
        resultado += caracter * 2

    # Mostrar el resultado
    print("\nResultado duplicado:")
    print(resultado)
