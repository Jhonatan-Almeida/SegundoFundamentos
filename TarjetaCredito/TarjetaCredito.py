"""
Enmascarador de Tarjetas de Crédito
Muestra solo los últimos 4 dígitos, el resto como asteriscos
"""

def enmascarar_tarjeta(numero_tarjeta: str) -> str:
    
    # Limpiar el número
    numero_limpio = ''.join(c for c in numero_tarjeta if c.isdigit())
    
    # Validar que tenga al menos 4 dígitos
    if len(numero_limpio) < 4:
        return "Número inválido"
    
    # Obtener últimos 4 dígitos
    ultimos_cuatro = numero_limpio[-4:]
    
    # Crear asteriscos para los dígitos ocultos
    asteriscos = '*' * (len(numero_limpio) - 4)
    
    return asteriscos + ultimos_cuatro

# Programa principal
if __name__ == "__main__":
    print("💳 ENMASCARADOR DE TARJETA DE CRÉDITO")
    print("=" * 40)
    
    # Pedir número de tarjeta
    numero = input("Introduce el número de tarjeta: ")
    
    # Enmascarar y mostrar resultado
    resultado = enmascarar_tarjeta(numero)
    
    print(f"\nNúmero original: {numero}")
    print(f"Número enmascarado: {resultado}")