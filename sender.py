import socket
import json

with open('config.json') as config_file:
  config = json.load(config_file)
  host = config['Browser_address']
  port=config['port']

def main():

  Browser_socket = socket.socket()
  Browser_socket.bind((host, port))
  Browser_socket.listen()
  print("Server listening on {}:{}".format(host, port))

  customer_socket, customer_address = Browser_socket.accept()
  print("Connection from:", customer_address)

  while True:
    message = customer_socket.recv(1024).decode()
    if not message:
      break
    print("Customer:", message)

    message = input("You: ")
    customer_socket.send(message.encode())

  customer_socket.close()
  Browser_socket.close()

if __name__ == '__main__':
  main()

