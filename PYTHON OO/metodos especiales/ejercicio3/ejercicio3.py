class Personaje:
    def __init__(self, nombre, fuerza, velocidad):
        self.nombre = nombre
        self.fuerza = fuerza
        self.velocidad = velocidad

    def __repr__(self):
        return f"Personaje({self.nombre} fuerza={self.fuerza}, velocidad={self.velocidad})"
    
    def __add__(self, otro):
        nuevo_nombre = self.nombre+ "-" +otro.nombre
        nueva_fuerza = ((self.fuerza + otro.fuerza)/2)**1.5
        nueva_velocidad = ((self.velocidad + otro.velocidad)/2)**1.5
        return Personaje(nuevo_nombre, nueva_fuerza, nueva_velocidad)
    
goku = Personaje("Goku", 8000, 7000)
vegeta = Personaje("Vegeta", 10000, 7500)

gogeta = goku + vegeta
print(gogeta)