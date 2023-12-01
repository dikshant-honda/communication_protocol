import socket

server_address = ('192.168.11.16', 12345)

try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    print(f"Connected to {server_address}")

    message = "Hello, server!"
    client_socket.send(message.encode())

except Exception as e:
    print(f"Error: {e}")

finally:
    client_socket.close()