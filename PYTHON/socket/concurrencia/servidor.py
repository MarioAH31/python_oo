# servidor_multicliente.py
import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

def manejar_cliente(conn, addr):
    print(f"🟢 Cliente conectado: {addr}")

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            mensaje = data.decode()
            print(f"{addr}: {mensaje}")

            respuesta = f"Servidor recibió: {mensaje}"
            conn.sendall(respuesta.encode())

    except Exception as e:
        print(f"⚠️ Error con {addr}: {e}")

    finally:
        conn.close()
        print(f"🔴 Cliente desconectado: {addr}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("🚀 Servidor concurrente escuchando...")

while True:
    conn, addr = server.accept()

    hilo = threading.Thread(
        target=manejar_cliente,
        args=(conn, addr),
        daemon=True
    )
    hilo.start()
