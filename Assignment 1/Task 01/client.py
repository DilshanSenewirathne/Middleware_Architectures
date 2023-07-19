import socket
import sys

def start_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_ip, server_port))
        print("Connected to server.")
        print("Type 'terminate' to end the connection.")

        while True:
            message = input("> ")
            client_socket.sendall(message.encode())

            if message.lower().strip() == "terminate":
                print("Connection terminated.")
                break

    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python client.py <server_ip> <server_port>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    start_client(server_ip, server_port)
