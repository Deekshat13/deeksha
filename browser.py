import socket
import threading
import json

clients = []

def handle_client(client_socket,client_address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8');

            print(f"Received from {client_address}: {message}")
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break
    client_socket.close()


def broadcast(message):
    for client in clients:
            try:
                client.send(message.encode('utf-8'))
            except:
                continue

def send_messages():
    while True:
        message = input("")
        if message=="bye":
            exit();
        formatted_message = f"Browser: {message}"
        broadcast(formatted_message)

def main():
    n = int(input("Enter how many clients you need to connect: "))
    with open('config.json') as config_file:
        config = json.load(config_file)
        host = config['Browser_address']
        port = config['port']

    Browser = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Browser.bind((host, port))
    Browser.listen(5)

    print(f"Server listening on {host}:{port}")
    send_thread = threading.Thread(target=send_messages)
    send_thread.start()

    for i in range(n):
        client_socket, client_address = Browser.accept()
        print(f"Accepted connection from {client_address}")
        clients.append(client_socket)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,client_address))
        client_thread.start()

if __name__ == "__main__":
    main()


