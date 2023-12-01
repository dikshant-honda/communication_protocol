import socket

server_address = ('0.0.0.0', 12345)

try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(server_address)
    server_socket.listen(1)

    print(f"Server listening on {server_address}")

    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")

except socket.error as e:
    print(f"Socket error: {e}")
except OSError as e:
    print(f"OS error: {e}")
except Exception as e:
    print(f"Error: {e}")

finally:
    client_socket.close()
    server_socket.close()
