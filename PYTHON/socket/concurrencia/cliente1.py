# cliente.py
import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Conectado al servidor")

try:
    while True:
        msg = input("Tú: ")
        client.sendall(msg.encode())

        data = client.recv(1024)
        print("Servidor:", data.decode())

except KeyboardInterrupt:
    print("\nSaliendo...")

finally:
    client.close()
