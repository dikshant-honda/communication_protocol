import socket

# HOST = "192.168.11.56"  # The server's hostname or IP address
# HOST = "dikshant.onthewifi.com"  # The server's hostname or IP address
HOST = "0b84-103-67-223-6.ngrok-free.app"  # The server's hostname or IP address
PORT = 12345  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")