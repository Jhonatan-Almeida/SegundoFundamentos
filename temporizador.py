import time as  t

temporador = int(input("Ingrese el tiempo en segundos para el temporizador: "))
print(f"Temporizador iniciado por {temporador} segundos.")
for i in range(temporador, 0, -1):
    print(i)
    t.sleep(1)
print("¡Tiempo terminado!")

