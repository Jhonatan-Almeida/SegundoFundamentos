"""
EJERCICIO DE BIENVENIDA

"""

def formatear_nombre(nombre: str) -> str:
    
    nombre_sin_puntos = nombre.replace('.', '')
    
    nombre_formateado = nombre_sin_puntos.capitalize()
    
    return nombre_formateado

def mostrar_versiones_mensaje(nombre: str, mensaje: str) -> None:
    
    print("\n--- RESULTADOS FINALES ---")
    
    
    print(f"a) ¡Hola, {nombre}, {mensaje}!")
    
    # MAYÚSCULAS
    print(f"b) ¡HOLA, {nombre.upper()}, {mensaje.upper()}!")
    
    # minúsculas
    print(f"c) ¡hola, {nombre.lower()}, {mensaje.lower()}!")

def main() -> None:
    """Función principal"""
    print("=" * 50)
    print("-------BIENVENIDO-------")
    print("=" * 50)
    
    
    mensaje_base = 'estas usando python'
    print(f"\n Mensaje base: '{mensaje_base}'")
    
    
    nombre_original = input("\n Por favor, introduce tu nombre: ")
    print(f"   Nombre original: {nombre_original}")
    
    # Formatear el nombre
    nombre_final = formatear_nombre(nombre_original)
    print(f"    Nombre formateado: {nombre_final}")
    
    
    mostrar_versiones_mensaje(nombre_final, mensaje_base)
    
    
    mensaje_final = mensaje_base.replace('python', 'Python')
    
 
    print(f"MENSAJE FINAL: ¡Hola, {nombre_final}, {mensaje_final}!")
    
    
    
if __name__ == "__main__":
    main()