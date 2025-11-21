# Script para calcular la cuenta de un restaurante
# Autor: Wendy

print("=== RESTAURANTE - CÁLCULO DE CUENTA ===")

# Precios del menú
precio_ensalada = 12
precio_sopa = 10
precio_dorada = 18
precio_arroz = 14
precio_lasana = 15
precio_brownie = 8
precio_helado = 6
precio_refresco = 5.5
precio_cafe = 3.5

# Leer cantidades consumidas (ahora con decimales)
ensalada = float(input("Cantidad de Ensalada mixta: "))
sopa = float(input("Cantidad de Sopa de pescado: "))
dorada = float(input("Cantidad de Dorada al horno: "))
arroz = float(input("Cantidad de Arroz al curry: "))
lasana = float(input("Cantidad de Lasaña de carne: "))
brownie = float(input("Cantidad de Brownie de chocolate: "))
helado = float(input("Cantidad de Helado: "))
refrescos = float(input("Cantidad de Refrescos: "))
cafe = float(input("Cantidad de Café: "))

# Cálculo del total
total = (ensalada * precio_ensalada +
         sopa * precio_sopa +
         dorada * precio_dorada +
         arroz * precio_arroz +
         lasana * precio_lasana +
         brownie * precio_brownie +
         helado * precio_helado +
         refrescos * precio_refresco +
         cafe * precio_cafe)

# Mostrar resultado final con dos decimales
print(f"\nWendy, el total a pagar es: {total:.2f} EU")
