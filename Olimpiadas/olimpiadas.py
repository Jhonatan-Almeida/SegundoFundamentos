"""
OLIMPIADAS TECNOECUATORIANO
"""

# Ingresar los tiempos
print("INGRESO DE TIEMPO FINAL")
print("=" * 40)

finalistas = ["Wilson Pascal", "Jhon Cano", "Wil Villota"]
resultados = []

for atleta in finalistas:
    print(f"\nTiempo de {atleta}:")
    minutos = int(input("   Minutos: "))
    segundos = int(input("   Segundos: "))
    Milisegundos = int(input("   Milisegundos: "))
    
    # Convertir a segundos
    tiempo_segundos = minutos * 60 + segundos + Milisegundos / 100
    
    # Calcular velocidad (100m pista)
    velocidad = 100 / tiempo_segundos
    
    resultados.append({
        'nombre': atleta,
        'tiempo_segundos': tiempo_segundos,
        'velocidad': velocidad
    })

# resultados
print("\nRESULTADOS FINALES")
print("=" * 50)
print(f"{'ATLETA':<20} {'TIEMPO (s)':<12} {'VELOCIDAD (m/s)':<15}")
print("-" * 50)

for resultado in resultados:
    print(f"{resultado['nombre']:<20} {resultado['tiempo_segundos']:<12.2f} {resultado['velocidad']:<15.2f}")

# Ganador
ganador = min(resultados, key=lambda x: x['tiempo_segundos'])
print(f"\nGANADOR: {ganador['nombre']} - {ganador['velocidad']:.2f} m/s")