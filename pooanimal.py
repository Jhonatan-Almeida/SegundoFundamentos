class Animal:
    # Propiedades
    def __init__(self, color, tamaño, peso, uñas_retractiles, colmillos, cuadrupedo=True):
        self.color = color
        self.tamaño = tamaño
        self.peso = peso
        self.uñas_retractiles = uñas_retractiles
        self.colmillos = colmillos
        self.cuadrupedo = cuadrupedo

    # Métodos
    def desplazarse(self, velocidad=50):
        print("El animal se está desplazando a una velocidad de ", velocidad, "km/h.")

    def masticar(self):
        print("El animal mastica su comida.")

    def digerir(self):
        print("El animal está digiriendo los alimentos.")

    def respirar(self):
        print("El animal está respirando.")

    def secretar_hormonas(self):
        print("El animal secreta hormonas para regular funciones corporales.")

    def parpadear(self):
        print("El animal parpadea para proteger y humedecer sus ojos.")

    # Método para mostrar todos los datos
    def mostrar_info(self):
        print("=== Información del animal ===")
        print(f"Color: {self.color}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Peso: {self.peso} kg")
        print(f"¿Uñas retráctiles?: {self.uñas_retractiles}")
        print(f"¿Tiene colmillos?: {self.colmillos}")
        print(f"¿Es cuadrúpedo?: {self.cuadrupedo}")
        print("==============================")


# Crear un objeto (instancia) de Animal
tigre = Animal(
    color="Negro",
    tamaño="Grande",
    peso=220,
    uñas_retractiles=True,
    colmillos=True,
    cuadrupedo=True
)

# Usar sus métodos
tigre.mostrar_info()
tigre.desplazarse(80)
tigre.masticar()
tigre.digerir()
tigre.respirar()
tigre.secretar_hormonas()
tigre.parpadear()
