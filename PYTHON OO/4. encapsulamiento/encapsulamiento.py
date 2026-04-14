class MiClase:
    def __init__(self):
        self.__atributo_privado = "valor"  # Atributo privado

objeto = MiClase()
print(objeto.__atributo_privado)  # Esto generará un error AttributeError