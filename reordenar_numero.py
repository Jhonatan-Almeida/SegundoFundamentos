# a.

numero = input("Introduce un número de más de una cifra: ")

print("Los dígitos son:")
for digito in numero:
    print(digito)

# b. 

numero = input("Introduce un número entero de 4 cifras: ")

if len(numero) != 4 or not numero.isdigit():
    print("Debes introducir exactamente un número de 4 cifras.")
else:
    invertido = numero[::-1]   # forma rápida de invertir un string
    print(f"El número invertido es: {invertido}")
