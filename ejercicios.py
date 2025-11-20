def mensaje_bienvenida():
    # MENSAJE DE BIENVENIDA
    mensaje = "estas usando python"
    print(mensaje)
    nombre = input("Introduce tu nombre: ")
    nombre = nombre.replace(".", "").capitalize()
    print(f"¡Hola, {nombre}, estas usando Python!")

def casa_de_cambios():
    # CASA DE CAMBIOS
    euros = float(input("Introduce cantidad de euros: "))
    tipo_cambio = 1.2
    bruto = euros * tipo_cambio
    tasa = bruto * 0.1
    neto = bruto - tasa
    print("\n=== DESGLOSE ===")
    print(f"Total en dólares: {bruto:.2f} $")
    print(f"Tasa de gestión (10%): {tasa:.2f} $")
    print(f"Dólares recibidos por usuario: {neto:.2f} $")

def olimpiadas_skeleton():
    # OLIMPIADAS
    distancia = 100
    print("Introduce los tiempos de los finalistas:")
    def tiempo_segundos(nombre):
        m = int(input(f"{nombre} - Minutos: "))
        s = int(input(f"{nombre} - Segundos: "))
        c = int(input(f"{nombre} - Centésimas: "))
        return m*60 + s + c/100
    t_h = tiempo_segundos("Hannah Neise")
    t_j = tiempo_segundos("Jackie Narracott")
    t_k = tiempo_segundos("Kimberley Bos")
    print("\n=== RESULTADOS ===")
    print(f"Hannah: {t_h:.2f} s | Velocidad: {distancia/t_h:.2f} m/s")
    print(f"Jackie: {t_j:.2f} s | Velocidad: {distancia/t_j:.2f} m/s")
    print(f"Kimberley: {t_k:.2f} s | Velocidad: {distancia/t_k:.2f} m/s")

def compania_automoviles():
    # COMPAÑÍA DE AUTOMÓVILES
    precios = {"RBM Serie 1": 20000, "RMB Serie Plus": 35000, "RBM Todoterreno": 60000}
    comisiones = {"RBM Serie 1": 0.03, "RMB Serie Plus": 0.05, "RBM Todoterreno": 0.07}
    cant_s1 = int(input("RBM Serie 1 vendidos: "))
    cant_splus = int(input("RMB Serie Plus vendidos: "))
    cant_todo = int(input("RBM Todoterreno vendidos: "))
    total = (cant_s1*precios["RBM Serie 1"]*comisiones["RBM Serie 1"] +
             cant_splus*precios["RMB Serie Plus"]*comisiones["RMB Serie Plus"] +
             cant_todo*precios["RBM Todoterreno"]*comisiones["RBM Todoterreno"])
    print(f"Comisión total del mes: {total:.2f} €")

def reordenar_numeros():
    # REORDENANDO NÚMEROS
    numero = input("Introduce un número de más de una cifra: ")
    print("Dígitos:")
    for d in numero:
        print(d)
    if len(numero) == 4:
        invertido = numero[::-1]
        print(f"Número invertido: {invertido}")

def restaurante():
    # RESTAURANTE
    menu = {
        "Ensalada mixta": 12,
        "Sopa de pescado": 10,
        "Dorada al horno": 18,
        "Arroz al curry": 14,
        "Lasaña de carne": 15,
        "Brownie de chocolate": 8,
        "Helado": 6,
        "Refrescos": 5.5,
        "Café": 3.5
    }
    total = 0
    for plato, precio in menu.items():
        cant = float(input(f"Cantidad de {plato} ({precio} €): "))
        total += cant*precio
    print(f"Total de la cuenta: {total:.2f} €")

def tarjeta_credito():
    # TARJETA DE CRÉDITO
    tarjeta = input("Introduce número de tarjeta: ").replace(" ", "")
    ultimos4 = tarjeta[-4:]
    ocultos = "*"*(len(tarjeta)-4)
    resultado = ""
    for i, c in enumerate(ocultos + ultimos4):
        if i % 4 == 0 and i != 0:
            resultado += " "
        resultado += c
    print("Tarjeta enmascarada:", resultado)

def repite_caracteres():
    # REPITE LOS CARACTERES
    texto = input("Introduce un string de 5 caracteres: ")
    if len(texto) != 5:
        print("Debe tener 5 caracteres.")
    else:
        print("Resultado:", "".join([c*2 for c in texto]))

def operaciones_aritmeticas():
    # OPERACIONES ARITMÉTICAS
    print("a. Resultado de (3 + 2**2 * 5)**2 =", (3 + 2**2 * 5)**2)
    n = int(input("b. Introduce un número entero positivo n: "))
    print(f"Suma de 1 a {n} =", n*(n+1)//2)
    a = int(input("c. Primer número: "))
    b = int(input("c. Segundo número: "))
    print(f"Números: {a}, {b} | Cociente: {a//b} | Resto: {a%b}")

def calculadora_ahorros():
    # CALCULADORA DE AHORROS
    nombre = input("Introduce tu nombre: ")
    print(f"Hola {nombre}")
    salario_hora = float(input("Salario por hora: "))
    horas_sem = float(input("Horas trabajadas por semana: "))
    salario_semanal = salario_hora*horas_sem
    ganancias_anuales = salario_semanal*52
    print(f"{nombre} tiene unas ganancias anuales de: {ganancias_anuales:.2f} €")
    gastos_sem = float(input("Gastos semanales: "))
    gasto_anual = gastos_sem*52
    ahorro_anual = ganancias_anuales - gasto_anual
    print(f"Gasto anual: {gasto_anual:.2f} € | Ahorro anual: {ahorro_anual:.2f} €")
    # Simulación tiempo parcial y gastos reducidos
    horas_parciales = 25
    gastos_reducidos = gastos_sem*0.75
    ganancias_parciales = salario_hora*horas_parciales*52
    ahorro_parcial = ganancias_parciales - gastos_reducidos*52
    print(f"\nSimulación 25 h/semana y gastos reducidos 3/4: Ahorro anual = {ahorro_parcial:.2f} €")
    print("Suficiente dinero para gastos?" , "Sí" if ahorro_parcial>=0 else "No")

# Menú principal
while True:
    print("\n=== MENÚ DE EJERCICIOS PYTHON ===")
    print("1. Mensaje de bienvenida")
    print("2. Casa de cambios")
    print("3. Olimpiadas Skeleton")
    print("4. Compañía de automóviles")
    print("5. Reordenando números")
    print("6. Restaurante")
    print("7. Tarjeta de crédito")
    print("8. Repite los caracteres")
    print("9. Operaciones aritméticas")
    print("10. Calculadora de ahorros")
    print("0. Salir")
    opcion = input("Elige una opción: ")
    if opcion=="1":
        mensaje_bienvenida()
    elif opcion=="2":
        casa_de_cambios()
    elif opcion=="3":
        olimpiadas_skeleton()
    elif opcion=="4":
        compania_automoviles()
    elif opcion=="5":
        reordenar_numeros()
    elif opcion=="6":
        restaurante()
    elif opcion=="7":
        tarjeta_credito()
    elif opcion=="8":
        repite_caracteres()
    elif opcion=="9":
        operaciones_aritmeticas()
    elif opcion=="10":
        calculadora_ahorros()
    elif opcion=="0":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
