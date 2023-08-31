import socket
import threading
import json

def receive_messages(customer_socket):
    while True:
        try:
                message = customer_socket.recv(1024).decode('utf-8')
                if message.lower()=="bye":
                    exit(0)
                print(message)
        except:
            print("Disconnected from Browser.")
            break
def main():
    with open('config.json') as config_file:
        config = json.load(config_file)
        host = config['Browser_address']
        port = config['port']
    customer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        customer.connect((host, port))

        print(f"Connected to Browser at {host}:{port}")

        receive_thread = threading.Thread(target=receive_messages, args=(customer,))
        receive_thread.start()

        while True:
            message = input("")
            customer.send(message.encode())
        customer.close()
    except:
        print("Unable to connect")

if __name__ == "__main__":
    main()





