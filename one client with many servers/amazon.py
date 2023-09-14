import socket
import threading
import json
import os

# Function to handle receiving messages from the client
def receive_messages(client_socket):
    while True:
        try:
            client_message = client_socket.recv(1024).decode()
            if client_message=="exit":
                os._exit(0)
            print(f"customer: {client_message}")
        except Exception as e:
            print(f"Error: {e}")
            break

# Server 1 Configuration
def load_config():
    with open("config.json") as config_file: 
	    config = json.load(config_file) 
	    host = config['amazon_ip'] 
	    port = config['amazon_port'] 
	    return host, port

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"amazon listening on {host}:{port}")

    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        try:
            server_message = input("")
            client_socket.send(f"amazon: {server_message}".encode())
            if server_message.lower() == "exit":
                os._exit(0)
        except Exception as e:
            print(f"Error: {e}")
            os._exit(0)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    host, port = load_config()
    start_server(host, port)
