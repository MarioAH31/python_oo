# chat_cliente.py
import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("🟢 Conectado al chat")

try:
    while True:
        msg = input("Tú: ")
        client.sendall(msg.encode())

        respuesta = client.recv(1024).decode()
        print("Servidor:", respuesta)

except Exception as e:
    print("Error:", e)

finally:
    client.close()
    print("🔴 Desconectado")
