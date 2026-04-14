class Animal:
    def comer(self):
        print("El animal está comiendo.")

class Ave(Animal):
    def volar(self):
        print("El animal está volando.")

class Mamifero(Animal):
    def amamantar(self):
        print("El animal está amamantando.")

class Murcielago(Mamifero, Ave):
    pass

ave = Ave()

ave.comer()
ave.volar()

print(Murcielago.mro())  # Muestra el orden de resolución de métodos