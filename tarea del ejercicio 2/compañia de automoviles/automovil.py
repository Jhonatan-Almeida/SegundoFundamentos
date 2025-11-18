# COMPAÑÍA DE AUTOMÓVILES - Cálculo de comisiones

# Precios y comisiones
precio_serie1 = 20000
precio_serie_plus = 30000
precio_todoterreno = 60000

com_serie1 = 0.03
com_serie_plus = 0.05
com_todoterreno = 0.07

print("=== CÁLCULO DE COMISIONES DEL MES ===")

# 1. Pedir datos al usuario
cant_serie1 = int(input("Número de coches RBM Serie 1 vendidos: "))
cant_serie_plus = int(input("Número de coches RMB Serie Plus vendidos: "))
cant_todoterreno = int(input("Número de coches RBM Todoterreno vendidos: "))

# 2. Cálculo de comisiones por tipo de coche
comision_serie1 = cant_serie1 * precio_serie1 * com_serie1
comision_serie_plus = cant_serie_plus * precio_serie_plus * com_serie_plus
comision_todoterreno = cant_todoterreno * precio_todoterreno * com_todoterreno

# 3. Total comisionado
total_comisiones = comision_serie1 + comision_serie_plus + comision_todoterreno

# 4. Mostrar resultados
print("\n---- RESULTADOS ----")
print(f"Comisión por RBM Serie 1: {comision_serie1:.2f} €")
print(f"Comisión por RMB Serie Plus: {comision_serie_plus:.2f} €")
print(f"Comisión por RBM Todoterreno: {comision_todoterreno:.2f} €")
print("---------------------")
print(f"TOTAL A COMISIONAR ESTE MES: {total_comisiones:.2f} €")
print("---------------------")

