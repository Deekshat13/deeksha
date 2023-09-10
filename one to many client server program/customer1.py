import socket
import threading
import json
import os

# Load server configuration from config.json
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        host = config['browser_address']
        port = config['port']
    return host, port
    
# Function to handle receiving messages from the server
def customer_receive(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print("Server has closed the connection.")
                os._exit(0)
            print(message)
        except:
            print("Disconnected from server.")
            break

# Main function for the customer1 client
def main():
    # Creating a socket connection
    host, port = load_config()
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    print(f"Connected to server at {host}:{port}")

    # Create a separate thread for receiving server messages
    receive_thread = threading.Thread(target=customer_receive, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("")
        client_socket.send(message.encode('utf-8'))

        if message.lower().strip() == 'exit':
            print("Closing the connection...")
            client_socket.close()
            os._exit(0)  # Exit the client program

if __name__ == "__main__":
    main()
