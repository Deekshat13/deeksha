import socket
import json

# Load server configuration from config.json
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
        host = config['flipkart_address']
        port = config['port']
    return host, port

# Connect to the server and handle communication
def main():
    # Load server configuration
    host, port = load_config()

    # Creating a socket and connect to the server
    customer_socket = socket.socket()
    customer_socket.connect((host, port))

    try:
        while True:
            # Get user input and send it to the server
            message = input("You: ")
            customer_socket.send(message.encode())

            # Check if the user wants to exit
            if message.lower().strip() == 'bye':
                print("Closing the connection.")
                customer_socket.send("bye".encode())  # Send "bye" to the server
                break

            # Receive and display the server's response
            response = customer_socket.recv(1024).decode()
            print("From Flipkart:", response)

            # Check if the server wants to exit
            if response.lower().strip() == 'bye':
                print("Flipkart has closed the connection.")
                break

    except KeyboardInterrupt:
        print("Connection closed by user.")

    # Close the socket when done
    customer_socket.close()

if __name__ == '__main__':
    main()
