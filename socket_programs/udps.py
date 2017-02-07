import socket
UDPSock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

listen_addr = ("10.1.1.0",21567)
UDPSock.bind(listen_addr)
msg="HI THIS IS CHETNA"
UDPSock.sendto(msg.encode('utf-8'),server)
data,addr=UDPSock.recvfrom(1024)
print data
UDPSock.close()