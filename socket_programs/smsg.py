import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "HELLO , WORLD !!"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE,(UDP_IP,UDP_PORT))
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
while True :
    data, addr =sock.recvfrom(1024)
    print addr
    print "received message:", data
    print "UDP TARGET IP:", UDP_IP
    print "UDP TARGET PORT:", UDP_PORT
    print "message" , MESSAGE
