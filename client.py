import socket,cv2, pickle,struct
import imutils
camera = False
if camera == True:
	vid = cv2.VideoCapture(0)
else:
	vid = cv2.VideoCapture('/home/dikshant/Videos/Leeds.mp4')
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host_ip = '192.168.30.139' # Here according to your server ip write the address

port = 9999
client_socket.connect((host_ip,port))

if client_socket: 
	while (vid.isOpened()):
		try:
			img, frame = vid.read()
			frame = imutils.resize(frame,width=380)
			a = pickle.dumps(frame)
			message = struct.pack("Q",len(a))+a
			sent = client_socket.sendall(message)
			if sent == 0:
				raise RuntimeError("socket connection broken")
			cv2.imshow(f"TO: {host_ip}",frame)
			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				client_socket.close()
		except:
			print('VIDEO FINISHED!')
			break

