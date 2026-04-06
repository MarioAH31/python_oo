# mini_http_server.py
import socket

HOST = "0.0.0.0"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"🌐 Servidor HTTP escuchando en http://localhost:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"Conexión de {addr}")

    request = conn.recv(1024).decode()
    print("REQUEST:")
    print(request)

    # Respuesta HTTP manual
    body = "<h1>Hola desde un servidor HTTP hecho a mano 😎</h1>"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(body.encode())}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{body}"
    )

    conn.sendall(response.encode())
    conn.close()

# http://localhost:8080
