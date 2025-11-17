
"""
Script para realizar operaciones aritméticas básicas
"""

def operacion_a():
    """Realiza la operación: ((3 + 2) / (2 * 5))²"""
    resultado = ((3 + 2) / (2 * 5)) ** 2
    print(f"a. Resultado de ((3 + 2) / (2 * 5))² = {resultado}")
    return resultado

def operacion_b():
    """Realiza la operación: n(n+1)/2 para un entero positivo n"""
    try:
        n = int(input("b. Introduce un número entero positivo n: "))
        if n <= 0:
            print("Error: El número debe ser positivo.")
            return None
        
        resultado = n * (n + 1) // 2
        print(f"   Resultado de {n}({n}+1)/2 = {resultado}")
        return resultado
    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")
        return None

def operacion_c():
    """Muestra cociente y resto de la división de dos números enteros"""
    try:
        num1 = int(input("c. Introduce el primer número entero: "))
        num2 = int(input("   Introduce el segundo número entero: "))
        
        if num2 == 0:
            print("   Error: No se puede dividir por cero.")
            return None
        
        cociente = num1 // num2
        resto = num1 % num2
        
        print(f"   Números: {num1} y {num2}")
        print(f"   Cociente: {num1} // {num2} = {cociente}")
        print(f"   Resto: {num1} % {num2} = {resto}")
        
        return cociente, resto
    except ValueError:
        print("Error: Por favor, introduce números enteros válidos.")
        return None

def main():
    """Función principal que ejecuta todas las operaciones"""
    print("=" * 50)
    print("      OPERACIONES ARITMÉTICAS")
    print("=" * 50)
    
    # Operación a
    operacion_a()
    print()
    
    # Operación b
    operacion_b()
    print()
    
    # Operación c
    operacion_c()
    print()
    
    print("Programa terminado.")

if __name__ == "__main__":
    main()