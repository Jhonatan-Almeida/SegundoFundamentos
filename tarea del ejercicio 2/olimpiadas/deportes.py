# OLIMPIADAS - Skeleton

print("INGRESE LOS TIEMPOS DE CADA FINALISTA")
print("(Formato: minutos, segundos, centésimas)\n")

# 1. Pedimos los tiempos al usuario
# HANNAH
min_h = int(input("Hannah Neise - Minutos: "))
seg_h = int(input("Hannah Neise - Segundos: "))
cen_h = int(input("Hannah Neise - Centésimas: "))

# JACKIE
min_j = int(input("\nJackie Narracott - Minutos: "))
seg_j = int(input("Jackie Narracott - Segundos: "))
cen_j = int(input("Jackie Narracott - Centésimas: "))

# KIMBERLEY
min_k = int(input("\nKimberley Bos - Minutos: "))
seg_k = int(input("Kimberley Bos - Segundos: "))
cen_k = int(input("Kimberley Bos - Centésimas: "))

# 2. Convertimos a segundos
hannah_seg = min_h * 60 + seg_h + cen_h / 100
jackie_seg = min_j * 60 + seg_j + cen_j / 100
kimberly_seg = min_k * 60 + seg_k + cen_k / 100

# 3. Cálculo de velocidad
distancia = 100  # metros

vel_hannah = distancia / hannah_seg
vel_jackie = distancia / jackie_seg
vel_kimberly = distancia / kimberly_seg

# 4. Resultados
print("\n----- RESULTADOS -----")
print(f"Hannah Neise:")
print(f"  Tiempo total: {hannah_seg:.2f} segundos")
print(f"  Velocidad media: {vel_hannah:.2f} m/s\n")

print(f"Jackie Narracott:")
print(f"  Tiempo total: {jackie_seg:.2f} segundos")
print(f"  Velocidad media: {vel_jackie:.2f} m/s\n")

print(f"Kimberley Bos:")
print(f"  Tiempo total: {kimberly_seg:.2f} segundos")
print(f"  Velocidad media: {vel_kimberly:.2f} m/s")
print("------------------------")
