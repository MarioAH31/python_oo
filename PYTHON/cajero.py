from datetime import datetime

def menu():
    print("Bienvenido al Cajero Automático")
    print("1. Registrar Usuario")
    print("2. Iniciar Sesión")
    print("3. Salir")

class Usuario:
    def __init__(self, nombre, edad, documento, PIN):
        self.nombre = nombre
        self.edad = edad
        self.documento = documento
        self.PIN = PIN
        self.listado_usuarios = []
    
class CuentaBancaria:
    def __init__(self, usuario, saldo_inicial=0):
        self.usuario = usuario
        self.saldo = saldo_inicial

    def registrar_usuario(self):
