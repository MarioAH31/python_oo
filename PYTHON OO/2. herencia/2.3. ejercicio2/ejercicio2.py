# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def mostrar_informacion(self):
#         print(f"Nombre: {self.nombre} \nEdad: {self.edad}")

# class Estudiante(Persona):
#     def __init__(self, nombre, edad, grado):
#         super().__init__(nombre, edad)
#         self.grado = grado

#     def mostrar_grado(self):
#         super().mostrar_informacion()
#         print(f"Grado: {self.grado}")

# estudiante = Estudiante("Ana", 20, "Segundo")
# estudiante.mostrar_grado()    
    
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad}")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado

    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

estudiante = Estudiante("Ana", 20, "Segundo")
estudiante.mostrar_informacion()
estudiante.mostrar_grado()    