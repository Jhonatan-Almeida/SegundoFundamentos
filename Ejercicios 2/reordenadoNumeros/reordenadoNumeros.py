"""
REORDENANDO NÚMEROS
"""

print(" REORDENANDO NÚMEROS")
print("=" * 30)


print("\n--- PARTE A: Descomposición ---")
numero_a = input("Introduce un número de más de una cifra: ")

print("Dígitos del número:")
for digito in numero_a:
    print(digito)

 
print("\n--- PARTE B: Reversión ---")
numero_b = input("Introduce un número de 4 cifras: ")


revertido = numero_b[::-1]
print(f"Original: {numero_b} → Revertido: {revertido}")