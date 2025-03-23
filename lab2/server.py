import socket
import threading
import queue

PORT = 5000
SERVER_IP = "127.0.0.1"

def RecvData(sock, recvPackets):
    """Handles incoming UDP data and stores it in a queue."""
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            recvPackets.put((data, addr))
        except socket.error as e:
            print(f"Socket error in RecvData: {e}")
            break

def RunServer():
    """Main function to run the UDP server."""
    print(f"Server hosting on IP -> {SERVER_IP}")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((SERVER_IP, PORT))
    except socket.error as e:
        print(f"Failed to create or bind socket: {e}")
        return  

    clients = set()
    recvPackets = queue.Queue()

    print("Server Running...")

    # Start receiving thread
    recv_thread = threading.Thread(target=RecvData, args=(s, recvPackets), daemon=True)
    recv_thread.start()

    try:
        while True:
            while not recvPackets.empty():
                try:
                    data, addr = recvPackets.get()
                    if addr not in clients:
                        clients.add(addr)
                        continue

                    data = data.decode("utf-8").strip()
                    if data.endswith("qqq"):
                        print(f"Client {addr} disconnected.")
                        clients.discard(addr)
                        continue

                    print(f"Received from {addr}: {data}")
                    
                    for c in clients:
                        if c != addr:
                            try:
                                s.sendto(data.encode("utf-8"), c)
                            except socket.error as e:
                                print(f"Error sending to {c}: {e}")

                except Exception as e:
                    print(f"Error processing received data: {e}")

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        s.close()
        print("Socket closed.")

if __name__ == "__main__":
    RunServer()
