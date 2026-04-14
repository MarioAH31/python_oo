# Clase base
class Animal:
    
    # Método que será sobrescrito por las clases hijas
    def sonido(self):
        pass

# Clase hija que hereda de Animal
class Gato(Animal):
    
    # Sobrescribe el método sonido
    def sonido(self):
        return "Miau"

# Otra clase hija que hereda de Animal
class Perro(Animal):
    
    # Sobrescribe el método sonido
    def sonido(self):
        return "Guau"

# Función que recibe un objeto Animal
def hacer_sonido(animal):
    # Aquí ocurre el enlace dinámico:
    # Python decide en tiempo de ejecución qué método sonido() usar
    print(animal.sonido())

# Creamos objetos de diferentes clases
gato = Gato()
perro = Perro()

# Llamamos a la misma función con objetos distintos
hacer_sonido(gato)   # Imprime: Miau
hacer_sonido(perro)  # Imprime: Guau