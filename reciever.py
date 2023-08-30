import socket
import json

with open('config.json') as config_file:
  config = json.load(config_file)
  host = config['Browser_address']
  port = config['port']


def main():
  customer_socket = socket.socket()
  customer_socket.connect((host, port))
  message = input("You: ")

  while message.lower().strip() != 'bye':
    customer_socket.send(message.encode())

    message = customer_socket.recv(1024).decode()

    print("Server:", message)
    message = input("You: ")

  customer_socket.close()


if __name__ == '__main__':
  main()
