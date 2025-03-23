import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def receive_messages(client_socket):
    """Function to receive messages from the server."""
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("Connection to server lost.")
            client_socket.close()
            break

def start_client():
    """Start the chat client."""
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print("Connected to the chat server.")
    
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
    
    while True:
        try:
            message = input()
            if message.lower() == 'exit':
                break
            client.send(message.encode('utf-8'))
        except:
            break
    
    client.close()

if __name__ == "__main__":
    start_client()
