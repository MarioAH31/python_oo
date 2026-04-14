class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona(nombre={self.nombre}, edad={self.edad})"
    
    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"
    
    def __add__(self, otra):
            nueva_edad = self.edad + otra.edad
            return Persona(f"{self.nombre} y {otra.nombre}", nueva_edad)
    
mario = Persona("Mario", 19)
alejandro = Persona("Alejandro", 19)

nueva_persona = mario + alejandro
print(nueva_persona.edad)