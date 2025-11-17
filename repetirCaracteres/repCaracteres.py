"""
DUPLICADOR DE CARACTERES
Duplica cada carácter de un string de entrada
"""

def duplicar_caracteres(texto: str) -> str:
    
    # Verificar que tenga 5 caracteres
    if len(texto) != 5:
        return "Error: El texto debe tener 5 caracteres"
    
    # Duplicar cada carácter
    return ''.join(caracter * 2 for caracter in texto)

# Programa principal
if __name__ == "__main__":
    print("🔄 DUPLICADOR DE CARACTERES")
    print("=" * 30)
    
    # Pedir entrada al usuario
    entrada = input("Introduce un string de 5 caracteres: ")
    
    # Procesar y mostrar resultado
    resultado = duplicar_caracteres(entrada)
    
    print(f"\nEntrada: {entrada}")
    print(f"Salida:  {resultado}")