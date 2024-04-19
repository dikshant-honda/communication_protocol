import socket

# Constants
UDP_PORT = 12345  # Same port used by the client

def main():
    # Create a UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        # Bind the socket to the local IP address and port
        server_socket.bind(('0.0.0.0', UDP_PORT))

        print("Server is listening...")

        while True:
            # Receive data from the client
            data, addr = server_socket.recvfrom(1024)
            print(f"Received '{data.decode()}' from {addr}")

            # Respond to the client
            response = "Message received!"
            server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
    main()
