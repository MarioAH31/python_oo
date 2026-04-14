class Persona:
    def __init__(self, nombre):
        self._nombre = nombre # Atributo privado

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, new_nombre):
        self._nombre = new_nombre

mario = Persona("Mario")
print(mario.get_nombre())  # Accediendo al atributo privado mediante el getter

mario.set_nombre("Alejandro")  # Modificando el atributo privado mediante el setter
print(mario.get_nombre())  # Verificando el cambio mediante el getter