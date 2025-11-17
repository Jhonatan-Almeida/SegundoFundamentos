"""
CALCULADORA DE CUENTA
"""

# Menú del restaurante
menu = {
    "Ensalada mixta": 12.0,
    "Sopa de pescado": 10.0,
    "Dorada al horno": 18.0,
    "Arroz al curry": 14.0,
    "Lasaña de carne": 15.0,
    "Brownie de chocolate": 8.0,
    "Helado": 6.0,
    "Refrescos": 5.5,
    "Café": 3.5
}

print("CALCULADORA DE CUENTA - RESTAURANTE")
print("=" * 45)

# Mostrar menú
print("\nMENÚ:")
for plato, precio in menu.items():
    print(f"• {plato} - {precio} €")

# Ingresar consumo
print("\nINGRESE CANTIDAD CONSUMIDA:")
total = 0.0

for plato, precio in menu.items():
    cantidad = int(input(f"{plato}: "))
    total += cantidad * precio

# Mostrar resultado
print(f"\nTOTAL DE LA CUENTA: {total:.2f} €")