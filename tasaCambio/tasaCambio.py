"""
CASA DE CAMBIOS

"""

def casa_cambios_completa():
    print("=" * 50)
    print("CASA DE CAMBIOS 'PYTHON EXCHANGE'")
    print("=" * 50)
    
    # Recibir cantidad de euros
    try:
        euros = float(input("\nIntroduce la cantidad en Euros (€) que deseas cambiar: "))
    except ValueError:
        print("Error: Por favor, introduce un número válido.")
        return
    
    # Validar que la cantidad sea positiva
    if euros <= 0:
        print("Error: La cantidad debe ser mayor que 0.")
        return
    
    
    TASA_CAMBIO = 1.2
    TASA_GESTION = 0.10  # 10%
    
    # Cálculos
    cambio_sin_tasas = euros * TASA_CAMBIO
    comision_casa = cambio_sin_tasas * TASA_GESTION
    dolares_final = cambio_sin_tasas - comision_casa
    
    
    print("\n" + "-" * 40)
    print("DESGLOSE DE LA OPERACIÓN:")
    print("-" * 40)
    
    print(f"\nCANTIDAD INTRODUCIDA: {euros:.2f} €")
    print(f"Tasa de cambio: 1 € = {TASA_CAMBIO} $")
    
    print(f"\nCAMBIO SIN TASAS: {cambio_sin_tasas:.2f} $")
    print(f"Comision ({TASA_GESTION*100}%): -{comision_casa:.2f} $")
    print("-" * 30)
    print(f"TOTAL A RECIBIR: {dolares_final:.2f} $")
    
    # Resumen
    print("\n" + "=" * 30)
    print(f"RESUMEN FINAL:")
    print(f"Por {euros:.2f} € recibes {dolares_final:.2f} $")
    print("=" * 30)

def main():
    """Función principal"""
    while True:
        print("\n" + "=" * 50)
        print("BIENVENIDO A CASA DE CAMBIOS")
        print("=" * 50)
        print("1. Cambiar euros a dólares")
        print("2. Salir")
        
        opcion = input("\nSelecciona una opción (1-2): ")
        
        if opcion == "1":
            casa_cambios_completa()
        elif opcion == "2":
            print("¡Gracias por usar nuestro servicio!")
            break
        else:
            print("Opcion no valida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    main()