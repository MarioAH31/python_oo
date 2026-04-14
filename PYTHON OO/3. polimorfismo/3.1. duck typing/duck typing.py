class Pato:
    def sonido(self):
        print("Quack!")

    def correr(self):
        print("El pato está corriendo.")
    
class Gallina:
    def sonido(self):
        print("Cluck!")

    def correr(self):
        print("La gallina está corriendo.")
    
class Persona:
    def atrapar(self, animal):
        animal.sonido()
        animal.correr()
        print(f"¡Atrapaste al/la {animal.__class__.__name__}!")

pato = Pato()
gallina = Gallina()
persona = Persona()

persona.atrapar(pato)
print("- - - - -")
persona.atrapar(gallina)