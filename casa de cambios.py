# Casa de cambios

# Tasa de cambio
TASA_DOLAR = 1.2
COMISION = 0.10  # 10%

# 1. Pedir cantidad
euros = float(input("Ingresa la cantidad de euros que deseas cambiar: "))

# 2. Calcular comisión
comision = euros * COMISION

# 3. Calcular euros después de la comisión
euros_netos = euros - comision

# 4. Convertir a dólares
dolares_finales = euros_netos * TASA_DOLAR

# 5. Mostrar desglose
print("\n----- DESGLOSE DE LA TRANSACCIÓN -----")
print(f"Euros entregados:          {euros:.2f} €")
print(f"Comisión (10%):            {comision:.2f} €")
print(f"Euros tras comisión:       {euros_netos:.2f} €")
print(f"Tipo de cambio:            1 EUR = {TASA_DOLAR} USD")
print(f"Dólares recibidos:         {dolares_finales:.2f} $")
print("----------------------------------------")
