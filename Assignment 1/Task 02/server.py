import socket
import threading

clients = {}

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break

            message = data.decode()
            client_type = clients[client_socket]
            if client_type == "PUBLISHER":
                for client, ctype in clients.items():
                    if ctype == "SUBSCRIBER":
                        client.sendall(message.encode())
        except Exception as e:
            print(f"Error: {e}")
            break

    del clients[client_socket]
    client_socket.close()

def main():
    host = '0.0.0.0'
    port = 5000
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        try:
            client_socket, client_address = server_socket.accept()
            client_type = client_socket.recv(1024).decode().upper()

            if client_type not in ("PUBLISHER", "SUBSCRIBER"):
                client_socket.close()
            else:
                clients[client_socket] = client_type
                print(f"New {client_type} connected: {client_address}")
                client_handler = threading.Thread(target=handle_client, args=(client_socket,))
                client_handler.start()

        except KeyboardInterrupt:
            print("Server shutting down...")
            break
        except Exception as e:
            print(f"Error: {e}")
            continue

if __name__ == "__main__":
    main()
