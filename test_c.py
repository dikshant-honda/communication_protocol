import socket

# Constants
UDP_PORT = 12345  # Same port used by the server

def main():
    # Get the server's public IP address and port
    server_ip = "126.211.16.229"
    server_port = 12345

    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        # Send data to the server
        message = "Hello, server!"
        client_socket.sendto(message.encode(), (server_ip, server_port))

        # Receive response from the server
        response, addr = client_socket.recvfrom(1024)
        print(f"Received '{response.decode()}' from {addr}")

if __name__ == "__main__":
    main()
