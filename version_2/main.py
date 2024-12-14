import socket
import threading
import os

# Global variables
clients = {}  # Track connected clients with their callsigns
chat_history_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "chat_history.txt")  # File to save chat history

# Function to handle incoming client connections
def handle_incoming_connections(server_socket):
    while True:
        client_socket, addr = server_socket.accept()
        callsign = client_socket.recv(1024).decode()  # Receive the callsign from the client
        clients[client_socket] = callsign
        print(f"{callsign} connected from {addr}")
        threading.Thread(target=handle_client, args=(client_socket, addr, callsign)).start()

# Function to handle an individual client
def handle_client(client_socket, addr, callsign):
    with client_socket:
        print(f"{callsign} ({addr}) is now connected.")
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    if message.strip() == "/exit":
                        print(f"{callsign} ({addr}) has disconnected.")
                        break
                    print(f"{callsign} ({addr}): {message}")
                    save_message(f"{callsign} ({addr}): {message}")
                    broadcast_message(f"{callsign}: {message}", client_socket)
                else:
                    break
            except:
                break
    client_socket.close()
    del clients[client_socket]

# Function to broadcast a message to all connected clients
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.sendall(message.encode())
            except:
                del clients[client]

# Function to save messages to a history file
def save_message(message):
    with open(chat_history_file, "a") as file:
        file.write(message + "\n")

# Function to send messages to a peer
def send_messages(peer_socket, callsign):
    while True:
        message = input(f"{callsign}: ")
        if message.strip() == "/exit":
            break
        peer_socket.sendall(message.encode())

# Function to start the server
def start_server(host, port, callsign):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    print("Type '/exit' to stop the server.")
    threading.Thread(target=handle_incoming_connections, args=(server_socket,)).start()

# Function to connect to a peer
def connect_to_peer(host, port, callsign):
    peer_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    peer_socket.connect((host, port))
    peer_socket.sendall(callsign.encode())  # Send the callsign to the server
    print(f"Connected to peer at {host}:{port}")
    threading.Thread(target=handle_client, args=(peer_socket, (host, port), callsign)).start()
    send_messages(peer_socket, callsign)

# Entry point
def main():
    print("Welcome to the enhanced peer-to-peer chat program.")
    is_server = input("Do you want to start a server? (y/n): ").lower() == 'y'
    host = input("Enter the host IP (default: 127.0.0.1): ") or "127.0.0.1"
    port = int(input("Enter the port (default: 12345): ") or 12345)
    callsign = input("Enter your callsign: ")

    if is_server:
        start_server(host, port, callsign)
    else:
        connect_to_peer(host, port, callsign)

if __name__ == "__main__":
    main()