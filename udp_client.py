import cv2
import socket
import math
import pickle

max_length = 65000
host = '126.194.110.41'
port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

camera = True
if camera == True:
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture('/home/dikshant/Videos/sample.mp4')

ret, frame = cap.read()

while ret:
    # compress frame
    retval, buffer = cv2.imencode(".jpg", frame)

    if retval:
        # convert to byte array
        buffer = buffer.tobytes()
        # get size of the frame
        buffer_size = len(buffer)

        num_of_packs = 1
        if buffer_size > max_length:
            num_of_packs = math.ceil(buffer_size/max_length)

        frame_info = {"packs":num_of_packs}

        # send the number of packs to be expected
        # print("Number of packs:", num_of_packs)
        sock.sendto(pickle.dumps(frame_info), (host, port))
        
        left = 0
        right = max_length

        for i in range(num_of_packs):
            # truncate data to send
            data = buffer[left:right]
            left = right
            right += max_length

            # send the frames accordingly
            sock.sendto(data, (host, port))
    
    ret, frame = cap.read()

print("done")