# chat_servidor.py
import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("🟢 Servidor de chat activo...")

conn, addr = server.accept()
print(f"Cliente conectado: {addr}")

try:
    while True:
        msg = conn.recv(1024).decode()
        if not msg:
            break

        print("Cliente:", msg)

        respuesta = input("Tú: ")
        conn.sendall(respuesta.encode())

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
    server.close()
    print("🔴 Chat cerrado")
