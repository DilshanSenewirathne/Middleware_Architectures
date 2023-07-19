import socket
import sys

def start_server(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(1)
        print(f"Server is listening on port {port}...")

        conn, addr = server_socket.accept()
        print(f"Connected to client: {addr[0]}:{addr[1]}")

        while True:
            data = conn.recv(1024).decode()
            if data.lower().strip() == "terminate":
                print("Client has terminated the connection.")
                break
            print(f"Received from client: {data}")

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
