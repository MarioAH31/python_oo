def menu():
    print("\n--- Menu de opciones ---")
    print("1. registrar estudiante")
    print("2. ver estudiantes")
    print("3. editar estudiante")
    print("4. eliminar estudiante")
    print("5. salir")

class Estudiante:
    def __init__(self, nombre, edad, nota_Matematicas, nota_Lenguaje, nota_Tecnologia):
        self.nombre = nombre
        self.edad = edad
        self.nota_Matematicas = nota_Matematicas
        self.nota_Lenguaje = nota_Lenguaje
        self.nota_Tecnologia = nota_Tecnologia
        self.listado = []

    def registrar_estudiante(self):
        nombre = input("\nIngrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        while edad < 5 or edad > 23:
            print("Edad inválida. Debe estar entre 5 y 23 años.")
            edad = int(input("Ingrese la edad del estudiante: "))
        nota_Matematicas = float(input("Ingrese la nota de Matemáticas del estudiante: "))
        while nota_Matematicas < 0 or nota_Matematicas > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
            nota_Matematicas = float(input("Ingrese la nota de Matemáticas del estudiante: "))
        nota_Lenguaje = float(input("Ingrese la nota de Lenguaje del estudiante: "))
        while nota_Lenguaje < 0 or nota_Lenguaje > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
            nota_Lenguaje = float(input("Ingrese la nota de Lenguaje del estudiante: "))
        nota_Tecnologia = float(input("Ingrese la nota de Tecnología del estudiante: "))
        while nota_Tecnologia < 0 or nota_Tecnologia > 5:
            print("Nota inválida. Debe estar entre 0 y 5.")
            nota_Tecnologia = float(input("Ingrese la nota de Tecnología del estudiante: "))
        self.listado.append({'nombre': nombre, 'edad': edad, 'nota_Matematicas': nota_Matematicas, 'nota_Lenguaje': nota_Lenguaje, 'nota_Tecnologia': nota_Tecnologia})
        print("Estudiante registrado exitosamente.")

    def ver_estudiantes(self):
        if not self.listado:
            print("\nNo hay estudiantes registrados.")
            return
        for estudiante in self.listado:
            print(f"\nNombre: {estudiante['nombre']}, Edad: {estudiante['edad']}, Nota Matemáticas: {estudiante['nota_Matematicas']}, Nota Lenguaje: {estudiante['nota_Lenguaje']}, Nota Tecnología: {estudiante['nota_Tecnologia']}")

    def editar_estudiante(self):
        nombre = input("\nIngrese el nombre del estudiante a editar: ")
        for estudiante in self.listado:
            if estudiante['nombre'] == nombre:
                nueva_edad = int(input("Ingrese la nueva edad del estudiante: "))
                while nueva_edad < 5 or nueva_edad > 23:
                    print("Edad inválida. Debe estar entre 5 y 23 años.")
                    nueva_edad = int(input("Ingrese la nueva edad del estudiante: "))
                nueva_nota_Matematicas = float(input("Ingrese la nueva nota de Matemáticas del estudiante: "))
                while nueva_nota_Matematicas < 0 or nueva_nota_Matematicas > 5:
                    print("Nota inválida. Debe estar entre 0 y 5.")
                    nueva_nota_Matematicas = float(input("Ingrese la nueva nota de Matemáticas del estudiante: "))
                nueva_nota_Lenguaje = float(input("Ingrese la nueva nota de Lenguaje del estudiante: "))
                while nueva_nota_Lenguaje < 0 or nueva_nota_Lenguaje > 5:
                    print("Nota inválida. Debe estar entre 0 y 5.")
                    nueva_nota_Lenguaje = float(input("Ingrese la nueva nota de Lenguaje del estudiante: "))
                nueva_nota_Tecnologia = float(input("Ingrese la nueva nota de Tecnología del estudiante: "))
                while nueva_nota_Tecnologia < 0 or nueva_nota_Tecnologia > 5:
                    print("Nota inválida. Debe estar entre 0 y 5.")
                    nueva_nota_Tecnologia = float(input("Ingrese la nueva nota de Tecnología del estudiante: "))
                estudiante['edad'] = nueva_edad
                estudiante['nota_Matematicas'] = nueva_nota_Matematicas
                estudiante['nota_Lenguaje'] = nueva_nota_Lenguaje
                estudiante['nota_Tecnologia'] = nueva_nota_Tecnologia
                print("Estudiante editado exitosamente.")
                return
        print("\nEstudiante no encontrado.")

    def eliminar_estudiante(self):
            nombre = input("\nIngrese el nombre del estudiante a eliminar: ")
            for estudiante in self.listado:
                if estudiante['nombre'] == nombre:
                    self.listado.remove(estudiante)
                    print("Estudiante eliminado exitosamente.")
                    return
            print("\nEstudiante no encontrado.")
        
def main():
    listado = Estudiante("", 0, 0.0, 0.0, 0.0)
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            listado.registrar_estudiante()
        elif opcion == '2':
            listado.ver_estudiantes()
        elif opcion == '3':
            listado.editar_estudiante()
        elif opcion == '4':
            listado.eliminar_estudiante()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor intente de nuevo.")

main()