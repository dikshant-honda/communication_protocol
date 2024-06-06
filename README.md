# Data transmission using UDP

### setup:

1. library installation
```bash
pip install sockets
pip install opencv-python
```

2. package setup
```bash
cd ~/catkin_ws/src/
catkin_create_pkg communication_protocol rospy roscpp
cd ~/catkin_ws/src/communication_protocol/src/
git clone https://github.com/dikshant-honda/communication_protocol.git
cd ~/catkin_ws/
catkin_make
```

3. server setup

   run `ifconfig` in the terminal and get the `ipv4` address. you will get output like this:
       
   
         docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
            inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
            ether 02:42:33:5d:fe:37  txqueuelen 0  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    
       eno1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
                ether e0:73:e7:11:a9:d3  txqueuelen 1000  (Ethernet)
                RX packets 0  bytes 0 (0.0 B)
                RX errors 0  dropped 0  overruns 0  frame 0
                TX packets 0  bytes 0 (0.0 B)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
                device interrupt 19  memory 0x92200000-92220000  
        
       enp1s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
                inet 10.109.40.75  netmask 255.255.252.0  broadcast 10.109.43.255
                inet6 fe80::1ce4:dcca:904c:d832  prefixlen 64  scopeid 0x20<link>
                ether e0:73:e7:11:a9:d4  txqueuelen 1000  (Ethernet)
                RX packets 264320050  bytes 341483532031 (341.4 GB)
                RX errors 2  dropped 1705496  overruns 87  frame 1
                TX packets 3001621  bytes 430049197 (430.0 MB)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
                device memory 0x92100000-9217ffff  
        
       lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
                inet 127.0.0.1  netmask 255.0.0.0
                inet6 ::1  prefixlen 128  scopeid 0x10<host>
                loop  txqueuelen 1000  (Local Loopback)
                RX packets 4639600  bytes 4703067291 (4.7 GB)
                RX errors 0  dropped 0  overruns 0  frame 0
                TX packets 4639600  bytes 4703067291 (4.7 GB)
                TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

       

     `ipv4` address will be under the `enp1s0`. currently, it is: `10.109.40.75`. note this ipv4 address


4. client setup
   
   a. edit _line 7_ in `udp_client.py` : `host = 'xxx.xxx.xxx.xxx'`

   replace this line with the ipv4 address obtained from the server setup. for example, in above case: `host = '10.109.40.75'`

   b. if camera is attached then set the camera variable in _line 12_ `camera = True`, else add video path to be processed in _line 16_

5. connect both PCs to same network (require two PCs: a. **server** (PC in control room), b. **client** (PC to which camera is attached)

6. run the process:

   
   a. on server side:

         cd ~/catkin_ws/src/communication_protocol/src/communication_protocol/
         python udp_server.py
 
    b. on client side:
    
         cd ~/catkin_ws/src/communication_protocol/src/communication_protocol/
         python udp_client.py

-------------------------------------------------------------------------------------------------------

### TO DO: transfer messages across PCs over different wifi networks
