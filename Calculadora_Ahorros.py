
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}")


dinero_por_hora = float(input("Introduce tu salario por hora en euros: "))
horas_semanales = float(input("Introduce tus horas trabajadas por semana: "))


salario_semanal = dinero_por_hora * horas_semanales


ganancias_anuales = salario_semanal * 52


print(f"{nombre} tiene unas ganancias anuales de: {ganancias_anuales:.2f} euros")


gastos_semanales = float(input("Introduce tus gastos semanales en euros: "))


gasto_anual = gastos_semanales * 52


ahorro_anual = ganancias_anuales - gasto_anual


print(f"Gasto anual: {gasto_anual:.2f} euros")
print(f"Ahorro anual: {ahorro_anual:.2f} euros")


horas_parciales = 25
gastos_reducidos = gastos_semanales * 0.75

salario_semanal_parcial = dinero_por_hora * horas_parciales
ganancias_parciales = salario_semanal_parcial * 52
gasto_anual_reducido = gastos_reducidos * 52
ahorro_parcial = ganancias_parciales - gasto_anual_reducido

print("\n=== Simulación tiempo parcial ===")
print(f"Gastos anuales reducidos: {gasto_anual_reducido:.2f} euros")
print(f"Ahorro anual trabajando 25 h/semana: {ahorro_parcial:.2f} euros")
if ahorro_parcial >= 0:
    print("Sí, tendría suficiente dinero para cubrir sus gastos.")
else:
    print("No, no tendría suficiente dinero para cubrir sus gastos.")
