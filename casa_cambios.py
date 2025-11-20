
euros = float(input("Introduce la cantidad en euros: "))

tasa_cambio = 1.2


monto_dolares = euros * tasa_cambio                   
tasa_gestion = monto_dolares * 0.10                   
dolares_finales = monto_dolares - tasa_gestion      

print("\n=== DESGLOSE DE LA TRANSACCIÓN ===")
print(f"Euros ingresados: {euros} €")
print(f"Tipo de cambio: 1 € = {tasa_cambio} $")
print(f"Total en dólares (antes de tasas): {monto_dolares:.2f} $")
print(f"Tasa de gestión (10%): {tasa_gestion:.2f} $")
print(f"Dólares recibidos por el usuario: {dolares_finales:.2f} $")
