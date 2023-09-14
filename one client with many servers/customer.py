import socket
import threading
import json
import os 

# Create a list to store server sockets
server_sockets = []

# Function to handle receiving messages from the server
def receive_messages(server_socket):
    while True:
        try:
            server_message = server_socket.recv(1024).decode()
            if not server_message:
                break

            print(server_message)
        except Exception as e:
            print(f"Error: {e}")
            break

# Function to send a message to multiple servers
def broadcast_message(message):
    for socket in server_sockets:
        try:
            socket.send(message.encode())
        except Exception as e:
            print(f"Error sending message: {str(e)}")

# Function to connect to a server, start a receive thread, and return the socket
def connect_to_server(host, port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.connect((host, port))
        print(f"Connected to {host}:{port}")
        
        # Start a thread to receive messages from the server
        server_thread = threading.Thread(target=receive_messages, args=(server_socket,))
        server_thread.start()

        server_sockets.append(server_socket)
        return server_socket
    except Exception as e:
        print(f"Error connecting to server {host}:{port}: {str(e)}")
        return None


def load_config():
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
        flipkart_host = config['flipkart_ip']
        flipart_port = config['flipkart_port']
        amazon_host = config['amazon_ip']
        amazon_port = config['amazon_port']
    return flipkart_host , flipart_port, amazon_host, amazon_port

def main():
    flipkart_host , flipart_port, amazon_host, amazon_port = load_config()

    # Connect to Server 1
    server1_socket = connect_to_server(flipkart_host , flipart_port)

    # Connect to Server 2
    server2_socket = connect_to_server(amazon_host, amazon_port)

    try:
        while True:
            message = input("")

            # Send the message to all server sockets in the list
            broadcast_message(message)

            if message.lower() == "exit":
                os._exit(0)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()



