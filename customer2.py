import socket
import threading
import json

with open('config.json') as config_file:
  config = json.load(config_file)
  host = config['Browser_address']
  port = config['port']


def receive_messages(Reciever_socket):
    while True:
        try:
                message = Reciever_socket.recv(1024).decode('utf-8')
                print(message)
        except:
            print("Disconnected from Browser.")
            break
def main():
    Reciever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        Reciever.connect((host, port))

        print(f"Connected to Browser at {host}:{port}")

        receive_thread = threading.Thread(target=receive_messages, args=(Reciever,))
        receive_thread.start()

        while True:
            message = input("")
            Reciever.send(message.encode('utf-8'))
        Reciever.close()
    except:
        print("Unable to Connect")

if __name__ == "__main__":
    main()


