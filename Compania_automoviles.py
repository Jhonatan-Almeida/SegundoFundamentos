print("=== CÁLCULO DE COMISIONES MENSUALES ===")

precio_serie1 = 20000
com_serie1 = 0.03

precio_serie_plus = 35000
com_serie_plus = 0.05

precio_todoterreno = 60000
com_todoterreno = 0.07


cant_serie1 = int(input("Número de RBM Serie 1 vendidos: "))
cant_serie_plus = int(input("Número de RMB Serie Plus vendidos: "))
cant_todoterreno = int(input("Número de RBM Todoterreno vendidos: "))

comision_s1 = cant_serie1 * precio_serie1 * com_serie1
comision_splus = cant_serie_plus * precio_serie_plus * com_serie_plus
comision_todo = cant_todoterreno * precio_todoterreno * com_todoterreno

comision_total = comision_s1 + comision_splus + comision_todo

print("\n===== RESULTADO =====")
print(f"Comisión por RBM Serie 1: {comision_s1:.2f} €")
print(f"Comisión por RMB Serie Plus: {comision_splus:.2f} €")
print(f"Comisión por RBM Todoterreno: {comision_todo:.2f} €")
print("-----------------------------------")
print(f"Comisión TOTAL del mes: {comision_total:.2f} €")
