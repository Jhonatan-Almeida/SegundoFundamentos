 # CALCULADORA DE AHORROS
# Autor: Wendy
# Programa completo siguiendo todas las instrucciones

print("=== CALCULADORA DE AHORROS ===")

# 1. Pedimos el nombre del usuario
nombre = input("Ingresa tu nombre: ")

# Saludo
print("\nHola", nombre)

# 2. Guardar ingresos por hora y horas trabajadas en variables
dinero_por_hora = float(input("\n¿Cuánto ganas por hora? "))
horas_semanales = float(input("¿Cuántas horas trabajas por semana? "))

# 3. Calcular salario semanal
salario_semanal = dinero_por_hora * horas_semanales

# 4. Calcular ganancias anuales
ganancias_anuales = salario_semanal * 52  # 52 semanas del año

# 5. Imprimir mensaje con ganancias anuales
print(f"\n{nombre} tiene unas ganancias anuales de: {ganancias_anuales:.2f} euros")

# 6. Pedir gastos semanales
gastos_semanales = float(input("\n¿Cuánto gastas a la semana? "))

# 7. Calcular gasto anual
gasto_anual = gastos_semanales * 52

# 9. Calcular ahorros anuales (ganancias - gastos)
ahorros_anuales = ganancias_anuales - gasto_anual

# 10. Imprimir resultados finales
print("\n=== RESULTADOS ANUALES ===")
print("Ganancias anuales:", ganancias_anuales)
print("Gastos anuales:", gasto_anual)
print("Ahorros anuales:", ahorros_anuales)

# ---------------- PARTE EXTRA ----------------
# ¿Tendría suficiente dinero trabajando 25 horas y con gastos reducidos a 3/4?

print("\n=== CÁLCULO A TIEMPO PARCIAL ===")

# Nuevos valores según la pista:
horas_parcial = 25
gastos_reducidos = gastos_semanales * 0.75

# Nuevo salario semanal
salario_semanal_parcial = dinero_por_hora * horas_parcial

# Nuevas ganancias anuales
ganancias_anuales_parcial = salario_semanal_parcial * 52

# Nuevo gasto anual
gasto_anual_reducido = gastos_reducidos * 52

# Nuevos ahorros
ahorros_parcial = ganancias_anuales_parcial - gasto_anual_reducido

print("\nHoras trabajadas a tiempo parcial:", horas_parcial)
print("Gastos semanales reducidos al 75%:", gastos_reducidos)
print("Ganancias anuales a tiempo parcial:", ganancias_anuales_parcial)
print("Gastos anuales reducidos:", gasto_anual_reducido)
print("Ahorros anuales a tiempo parcial:", ahorros_parcial)

# Determinar si le alcanza o no
if ahorros_parcial >= 0:
    print("\nSí, trabajando a tiempo parcial y reduciendo gastos le alcanza para vivir.")
else:
    print("\nNo, trabajando a tiempo parcial NO le alcanza para cubrir sus gastos.")
