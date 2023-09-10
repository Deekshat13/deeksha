import socket
import threading
import json
import os  # Import the os module

# List to store client sockets
clients = []

# Load server configuration from config.json
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        host = config['browser_address']
        port = config['port']
    return host, port

# Function to handle messages from clients
def handle_client(client_socket, client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            # Check if the client wants to exit
            if message.strip().lower() == "bye":
                print(f"Client {client_address} requested to exit.")
                break
            print(f"Received from {client_address}: {message}")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break

    # Remove the client from the list
    clients.remove(client_socket)
    client_socket.close()

# Function to send messages to all connected clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            print("Unable to send the message")

# Function to send messages from the server
def send_messages():
    while True:
        message = input("")
        if message.lower() == "exit":
            print("Server is closing.")
            os._exit(0)  # Exit the entire program using os._exit
        formatted_message = f"Server: {message}"
        broadcast(formatted_message)

# Main function
def main():
    # Creating socket connection
    host, port = load_config()
    browser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    browser_socket.bind((host, port))
    browser_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    # Create a separate thread for sending server messages
    send_thread = threading.Thread(target=send_messages)
    send_thread.start()

    while True:
        client_socket, client_address = browser_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Add the client socket to the list
        clients.append(client_socket)

        # Create a separate thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    main()
