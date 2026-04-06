class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
       self.__nombre = nuevo_nombre

    @nombre.deleter
    def nombre(self):
        del self.__nombre   
    
persona = Persona("Mario")
print(persona.nombre) 

persona.nombre = "Luigi"  # Esto generará un AttributeError
print(persona.nombre)  

del persona.nombre  # print(persona.nombre) Esto generará un AttributeError

print("Operaciones completadas.")