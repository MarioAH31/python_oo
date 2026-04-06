class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} de {self.edad} años y grado {self.grado} está estudiando.")

nombre = input("Ingrese el nombre del estudiante: ")
edad = int(input("Ingrese la edad del estudiante: "))   
grado = input("Ingrese el grado del estudiante: ")

estudiante = Estudiante(nombre, edad, grado)

while True:
    estudiar = input("¿Desea que el estudiante estudie? (si/no): ")
    if estudiar.lower() == 'si':
        estudiante.estudiar()
        break
    elif estudiar.lower() == 'no':
        print("Programa terminado.")
        break
