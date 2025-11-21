# EJERCICIO A: Mostrar los componentes de un número

numero = input("Introduce un número de más de una cifra: ")

print("\n--- Dígitos del número ---")
for digito in numero:
    print(digito)

4
5
3
2

# EJERCICIO B: Invertir un número de cuatro cifras

numero = input("Introduce un número entero de cuatro cifras: ")

if len(numero) != 4 or not numero.isdigit():
    print("Error: Debes ingresar un número de EXACTAMENTE 4 cifras.")
else:
    invertido = numero[::-1]   # invertir la cadena
    print("\nEl número invertido es:", invertido)

2354
