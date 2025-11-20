print("=== CÁLCULO DE CUENTA DEL RESTAURANTE ===")


ensalada = 12
sopa = 10
dorada = 18
arroz = 14
lasagna = 15
brownie = 8
helado = 6
refresco = 5.5
cafe = 3.5


cant_ensalada = float(input("Cantidad de Ensalada mixta (12€): "))
cant_sopa = float(input("Cantidad de Sopa de pescado (10€): "))
cant_dorada = float(input("Cantidad de Dorada al horno (18€): "))
cant_arroz = float(input("Cantidad de Arroz al curry (14€): "))
cant_lasagna = float(input("Cantidad de Lasaña de carne (15€): "))
cant_brownie = float(input("Cantidad de Brownie de chocolate (8€): "))
cant_helado = float(input("Cantidad de Helado (6€): "))
cant_refresco = float(input("Cantidad de Refrescos (5.5€): "))
cant_cafe = float(input("Cantidad de Café (3.5€): "))


total = (
    cant_ensalada * ensalada +
    cant_sopa * sopa +
    cant_dorada * dorada +
    cant_arroz * arroz +
    cant_lasagna * lasagna +
    cant_brownie * brownie +
    cant_helado * helado +
    cant_refresco * refresco +
    cant_cafe * cafe
)


print("\n=== TOTAL DE LA CUENTA ===")
print(f"Total a pagar: {total:.2f} €")
