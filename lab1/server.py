import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

clients = []
clients_lock = threading.Lock()

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    
    with clients_lock:
        clients.append(client_socket)

    try:
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if not message:
                    break
                print(f"[{client_address}] {message}")
                broadcast(message, client_socket)
            except UnicodeDecodeError:
                print(f"[ERROR] Received a message with invalid encoding from {client_address}. Ignoring it.")
            except socket.error as e:
                print(f"[SOCKET ERROR] {client_address} encountered an error: {e}")
                break
    except Exception as e:
        print(f"[ERROR] Unexpected error with {client_address}: {e}")
    
    finally:
        with clients_lock:
            if client_socket in clients:
                clients.remove(client_socket)

        client_socket.close()
        print(f"[DISCONNECTED] {client_address} has left the chat.")

def broadcast(message, sender_socket):
    with clients_lock:
        for client in clients:
            if client != sender_socket:
                try:
                    client.send(message.encode('utf-8'))
                except socket.error:
                    print(f"[ERROR] Failed to send message to a client. Removing client.")
                    clients.remove(client)

def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allows rebinding the port
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
        
        while True:
            try:
                client_socket, client_address = server.accept()
                thread = threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True)
                thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            except socket.error as e:
                print(f"[ERROR] Error accepting a new connection: {e}")

    except Exception as e:
        print(f"[FATAL ERROR] Server encountered an issue: {e}")

    finally:
        server.close()
        print("[SERVER SHUTDOWN] Server has been closed.")

if __name__ == "__main__":
    start_server()
