import socket
import threading

## How to use:



def handle_incoming_connections(server_socket):
    while True:
        client_socket, addr = server_socket.accept()
        print(f"Connected by {addr}")
        threading.Thread(target=handle_client, args=(client_socket,)).start()

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"Peer: {message}")
            else:
                break
        except:
            break
    client_socket.close()

def send_messages(peer_socket):
    while True:
        message = input()
        peer_socket.sendall(message.encode())

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    threading.Thread(target=handle_incoming_connections, args=(server_socket,)).start()

def connect_to_peer(host, port):
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peer_socket.connect((host, port))
    print(f"Connected to peer at {host}:{port}")
    threading.Thread(target=send_messages, args=(peer_socket,)).start()
    handle_client(peer_socket)

print("Welcome to the peer-to-peer chat program")
is_server = input("Do you want to start a server? (y/n): ").lower() == 'y'

host = '127.0.0.1'
port = 12345

if is_server:
    start_server(host, port)
else:
    connect_to_peer(host, port)