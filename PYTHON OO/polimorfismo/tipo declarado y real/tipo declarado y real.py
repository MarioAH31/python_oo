class Animal:
    def sonido(self):
        return "Sonido genérico"

class Gato(Animal):
    def sonido(self):
        return "Miau"

# Tipo declarado: Animal
# Tipo real: Gato
animal = Gato()

print(animal.sonido()) # Salida: Miau
