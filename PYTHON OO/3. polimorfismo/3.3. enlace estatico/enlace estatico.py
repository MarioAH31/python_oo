# Definimos una clase simple
class Calculadora:

    # Método normal (no se sobrescribe)
    def sumar(self, a, b):
        # Retorna la suma de dos números
        return a + b

# Creamos un objeto de la clase Calculadora
calc = Calculadora()

# Llamamos directamente al método sumar
# Python sabe exactamente qué método ejecutar
print(calc.sumar(3, 5))  # Salida: 8