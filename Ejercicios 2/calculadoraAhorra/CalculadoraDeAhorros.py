
"""
CALCULADORA DE AHORROS ANUALES
Programa para calcular los ahorros anuales basado en ingresos y gastos
"""

def main():
    """Función principal de la calculadora de ahorros"""
    
    # 1. Solicitar nombre y saludar
    nombre = input("Por favor, introduce tu nombre: ")
    print(f"\n¡Hola {nombre}!")
    print("=" * 40)
    
    # 2. Obtener información de ingresos
    print("\n--- INGRESOS SEMANALES ---")
    try:
        # Dinero ganado por hora
        dinero_por_hora = float(input("Introduce tu salario por hora (€): "))
        
        # Horas trabajadas por semana
        horas_semanales = float(input("Introduce las horas trabajadas por semana: "))
        
    except ValueError:
        print("Error: Por favor, introduce valores numéricos válidos.")
        return
    
    # 3. Calcular salario semanal
    salario_semanal = dinero_por_hora * horas_semanales
    print(f"\nSalario semanal: {salario_semanal:.2f} €")
    
    # 4. Calcular ganancias anuales
    semanas_anuales = 52
    ganancias_anuales = salario_semanal * semanas_anuales
    
    # 5. Mostrar ganancias anuales
    print(f"\n{nombre} tiene unas ganancias anuales de: {ganancias_anuales:.2f} €")
    
    # 6. Obtener gastos semanales
    print("\n--- GASTOS SEMANALES ---")
    try:
        gastos_semanales = float(input("Introduce tus gastos semanales (€): "))
    except ValueError:
        print("Error: Por favor, introduce un valor numérico válido.")
        return
    
    # 7. Calcular gasto anual
    gastos_anuales = gastos_semanales * semanas_anuales
    print(f"Gastos anuales: {gastos_anuales:.2f} €")
    
    # 9. Calcular ahorros anuales
    ahorros_anuales = ganancias_anuales - gastos_anuales
    
    # 10. Mostrar resultados
    print("\n" + "=" * 50)
    print("          RESUMEN ANUAL")
    print("=" * 50)
    print(f"Ganancias anuales: {ganancias_anuales:.2f} €")
    print(f"Gastos anuales:    {gastos_anuales:.2f} €")
    print(f"AHORROS ANUALES:   {ahorros_anuales:.2f} €")
    
    
    if ahorros_anuales > 0:
        print(f"\n¡Felicidades {nombre}! Tienes capacidad de ahorro.")
    elif ahorros_anuales == 0:
        print(f"\n{nombre}, estás en equilibrio financiero.")
    else:
        print(f"\nAtención {nombre}, tienes déficit financiero.")
    
    
    print("\n" + "=" * 50)
    print("    ESCENARIO TIEMPO PARCIAL")
    print("=" * 50)
    
    # Nuevas condiciones: 25 horas semanales y gastos reducidos a 3/4
    nuevas_horas_semanales = 25
    nuevos_gastos_semanales = gastos_semanales * 0.75  # 3/4 de los gastos originales
    
    # Calcular nuevo escenario
    nuevo_salario_semanal = dinero_por_hora * nuevas_horas_semanales
    nuevas_ganancias_anuales = nuevo_salario_semanal * semanas_anuales
    nuevos_gastos_anuales = nuevos_gastos_semanales * semanas_anuales
    nuevos_ahorros_anuales = nuevas_ganancias_anuales - nuevos_gastos_anuales
    
    print(f"Horas trabajadas: {nuevas_horas_semanales} h/semana")
    print(f"Gastos reducidos al 75%: {nuevos_gastos_semanales:.2f} €/semana")
    print(f"Nuevo salario semanal: {nuevo_salario_semanal:.2f} €")
    print(f"Nuevas ganancias anuales: {nuevas_ganancias_anuales:.2f} €")
    print(f"Nuevos gastos anuales: {nuevos_gastos_anuales:.2f} €")
    print(f"NUEVOS AHORROS ANUALES: {nuevos_ahorros_anuales:.2f} €")
    
    # Evaluar si es suficiente para cubrir gastos
    if nuevas_ganancias_anuales >= nuevos_gastos_anuales:
        print(f"\nCon trabajo a tiempo parcial SÍ tienes suficiente dinero para tus gastos.")
        print(f"   Te sobrarían {nuevos_ahorros_anuales:.2f} € anuales.")
    else:
        print(f"\nCon trabajo a tiempo parcial NO tienes suficiente dinero para tus gastos.")
        print(f"   Te faltarían {abs(nuevos_ahorros_anuales):.2f} € anuales.")

if __name__ == "__main__":
    main()