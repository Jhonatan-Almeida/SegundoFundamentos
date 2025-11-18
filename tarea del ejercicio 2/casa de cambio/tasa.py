# CASA DE CAMBIOS

# 1. Pedimos al usuario la cantidad de euros
euros = float(input("Ingrese la cantidad de euros a cambiar: "))

# Tasa de cambio
tasa_cambio = 1.2  # 1 euro = 1.2 dólares

# Conversión total a dólares
dolares_totales = euros * tasa_cambio

# 2. Cálculo de tasas de gestión (10%)
tasa_gestion = dolares_totales * 0.10
dolares_usuario = dolares_totales - tasa_gestion

# Impresión del desglose
print("\n----- DESGLOSE DEL CAMBIO -----")
print(f"Euros ingresados: {euros:.2f} €")
print(f"Equivalente en dólares: {dolares_totales:.2f} $")
print(f"Tasa de gestión (10%): {tasa_gestion:.2f} $")
print(f"Dólares que recibirá el usuario: {dolares_usuario:.2f} $")
print("--------------------------------")


