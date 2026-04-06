class TanqueCombustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        self.combustible += cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible -= cantidad

class Auto:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print(f"El auto se ha movido exitosamente.")
        else:
            print("No hay suficiente combustible para mover el auto.")

    def obtener_posicion(self):
        return self.posicion
    
tanque = TanqueCombustible()
auto = Auto(tanque)

print(f"Posición inicial del auto: {auto.obtener_posicion()}")
auto.mover(50)
print(f"Posición del auto después de mover: {auto.obtener_posicion()}")
auto.mover(100)
print(f"Posición del auto después de mover: {auto.obtener_posicion()}")
auto.mover(200)
print(f"Posición del auto después de mover: {auto.obtener_posicion()}")