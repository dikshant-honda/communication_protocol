import socket
import cv2
import pickle
import struct
import threading
import pyshine as ps
import cv2
import timeit

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = socket.gethostname()
host_ip = '0.0.0.0'
print('HOST IP:', host_ip)
port = 12345
socket_address = (host_ip, port)
server_socket.bind(socket_address)
server_socket.listen()
print("Listening at", socket_address)


def show_client(addr, client_socket):
    try:
        print('CLIENT {} CONNECTED!'.format(addr))
        
        if client_socket:
            data = b""
            payload_size = struct.calcsize("Q")
            while True:
                start = timeit.default_timer()
                while len(data) < payload_size:
                    packet = client_socket.recv(4*1024)
                    if not packet:
                        raise RuntimeError("socket connection broken")
                    data += packet

                packed_msg_size = data[:payload_size]
                data = data[payload_size:]
                msg_size = struct.unpack("Q", packed_msg_size)[0]

                while len(data) < msg_size:
                    data += client_socket.recv(4*1024)

                print("time taken ", timeit.default_timer() - start, " seconds")
                
                frame_data = data[:msg_size]
                data = data[msg_size:]
                frame = pickle.loads(frame_data)
                text = f"CLIENT: {addr}"
                frame = ps.putBText(frame, text, 10, 10, vspace=10, hspace=1, font_scale=0.7, background_RGB=(
                    255, 0, 0), text_RGB=(255, 250, 250))
                cv2.imshow(f"FROM {addr}", frame)
                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    break
            client_socket.close()
    except Exception as e:
        print(f"CLIENT {addr} DISCONNECTED")
        pass


while True:
    client_socket, addr = server_socket.accept()
    thread = threading.Thread(target=show_client, args=(addr, client_socket))
    thread.start()
    print("TOTAL CLIENTS ", threading.activeCount() - 1)
