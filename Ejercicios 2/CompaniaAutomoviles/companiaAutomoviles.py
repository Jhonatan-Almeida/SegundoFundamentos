"""
SISTEMA DE COMISIONES
"""

# Datos de los automoviles
automoviles = {
    "RBM Serie 1": {"precio": 20000, "comision": 0.03},
    "RMB Serie plus": {"precio": 35000, "comision": 0.05},
    "RBM todoterreno": {"precio": 60000, "comision": 0.07}
}

print("SISTEMA DE CÁLCULO DE COMISIONES")
print("=" * 40)

# Pedir número de automoviles vendidos
ventas = {}
for modelo in automoviles:
    cantidad = int(input(f"\n¿Cuántos {modelo} se vendieron?: "))
    ventas[modelo] = cantidad

# Calcular las comisiones
total_comision = 0

print("\n RESULTADOS:")
print("=" * 50)

for modelo, cantidad in ventas.items():
    precio = automoviles[modelo]["precio"]
    porcentaje = automoviles[modelo]["comision"]
    
    venta_total = cantidad * precio
    comision = venta_total * porcentaje
    total_comision += comision
    
    print(f"\n{modelo}:")
    print(f"  • Unidades: {cantidad}")
    print(f"  • Venta total: {venta_total:,.2f} €")
    print(f"  • Comisión ({porcentaje*100}%): {comision:,.2f} €")

# 3. Mostrar total

print(f"COMISIÓN TOTAL DEL MES: {total_comision:,.2f} €")
