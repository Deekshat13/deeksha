import socket
import json

# Loading server configuration from config.json
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        host = config['flipkart_address']
        port = config['port']
    return host, port

# Main server function
def main():
    host, port = load_config()

    # Creating a socket connection
    flipkart_socket = socket.socket()
    flipkart_socket.bind((host, port))
    flipkart_socket.listen()
    print("Server listening on {}:{}".format(host, port))

    # Accepting client connection
    customer_socket, customer_address = flipkart_socket.accept()
    print("Connection from:", customer_address)

    while True:
        # Receive and display messages from the client
        message = customer_socket.recv(1024).decode()
        if not message:
            break
        print("From Customer:", message)

        if message.lower() == "bye":
            print("Client requested to terminate the connection.")
            break

        # Take user input and send it to the client
        response = input("You: ")
        customer_socket.send(response.encode())
        if response.lower() == "bye":
            print("server is closing.")
            break
        

    # Closing the client and server sockets
    customer_socket.close()
    flipkart_socket.close()

if __name__ == '__main__':
    main()
