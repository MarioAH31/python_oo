class A:
    def hablar(self):
        print("Hola desde A")

class B:
    def hablar(self):
        print("Hola desde B")

class C:
    def hablar(self):
        print("Hola desde C")

class D(B, C):
    def hablar(self):
        print("Hola desde D")

d = D()
d.hablar()  # Llama al método hablar de D