embarcaciones = [
    "Barco de pesca", #0
    "Yate de lujo", #1
    "Velero", #2
    "Crucero", #3
    "Lancha rápida" #4
    ]

print (embarcaciones[2])  
print(type(embarcaciones))  #Lista
print(type(embarcaciones[0])) #String
print(len(embarcaciones))  #Cantidad de elementos en la lista

busqueda = 'Barquito'
if  busqueda in embarcaciones:
    print(f'Si se encuentra la embarcacion: {busqueda}') 
    print("Si se encuentra la embarcacion: ", busqueda)
else:
    print(f'No se encuentra la embarcacion: {busqueda}') 
    print("No se encuentra la embarcacion: ", busqueda)

coches = ["BMW", "Audi", "Renault"]

if coches:
    print("La lista tiene elementos")

else:
    print("La lista esta vacia")

for barco in embarcaciones:
    print("El tipo de barco es: ", barco)

for barco in range(len(embarcaciones)):
    print("El tipo de barco es: ", embarcaciones[barco])