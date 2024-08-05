# Tcp server that listens on port 9999

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


print(socket.gethostname()) # get hostname
print(socket.gethostbyname(socket.gethostname())) # get ip address of hostname
print(socket.gethostbyname('localhost')) # get ip address of localhost

# bind to ip address and port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345)) 

#put the socket into listening mode

server_socket.listen()

# https://www.youtube.com/watch?v=7gek0eCnbHs&ab_channel=zuni
# STOPED AT 33:50