# Script para ocultar número de tarjeta de crédito
# Autor: Wendy

print("=== OCULTAR TARJETA DE CRÉDITO ===")

# Leer tarjeta como texto EXACTAMENTE como la escriba el usuario
tarjeta = input("Ingresa el número de la tarjeta (con espacios): ")

# Eliminar espacios para trabajar internamente
solo_digitos = tarjeta.replace(" ", "")

# Verificar que hay al menos 4 dígitos
if len(solo_digitos) < 4:
    print("Número de tarjeta inválido.")
else:
    # Últimos 4 dígitos de la tarjeta
    ultimos4 = solo_digitos[-4:]

    # Generar asteriscos para los demás
    ocultos = "*" * (len(solo_digitos) - 4)

    # Unir los asteriscos con los últimos 4 números
    tarjeta_oculta = ocultos + ultimos4

    # Volver a poner espacios cada 4 caracteres
    tarjeta_formateada = " ".join(
        tarjeta_oculta[i:i+4] for i in range(0, len(tarjeta_oculta), 4)
    )

    # Imprimir el resultado final
    print("\nTarjeta ocultada:")
    print(tarjeta_formateada)


