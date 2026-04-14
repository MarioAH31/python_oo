class Celular():
    def __init__(self, marca, modelo, almacenamiento):
        self.marca = marca
        self.modelo = modelo
        self.almacenamiento = almacenamiento

    def llamar(self):
        print(f"Estas llamando desde un {self.modelo}")

    def colgar(self):
        print(f"Has colgado la llamada en un {self.modelo}")    
        
celular1 = Celular("Samsung", "Galaxy S21", "128GB")
celular2 = Celular("Apple", "iPhone 13", "256GB")
print(celular1.marca)
print(celular2.marca)

celular1.llamar()
celular2.colgar()
