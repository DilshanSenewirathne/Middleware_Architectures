import socket
import sys

def main():
    if len(sys.argv) != 4:
        print("Usage: python client.py <server_ip> <server_port> <PUBLISHER/SUBSCRIBER>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client_type = sys.argv[3].upper()

    if client_type not in ("PUBLISHER", "SUBSCRIBER"):
        print("Invalid client type. Use PUBLISHER or SUBSCRIBER.")
        sys.exit(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, server_port))
        client_socket.sendall(client_type.encode())

        if client_type == "PUBLISHER":
            print("You are in PUBLISHER mode. Type 'terminate' to quit.")
            while True:
                message = input()
                if message.lower() == "terminate":
                    break
                client_socket.sendall(message.encode())
        else:
            print("You are in SUBSCRIBER mode. Type 'terminate' to quit.")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(data.decode())
                if data.decode().lower() == "terminate":
                    break

    except KeyboardInterrupt:
        print("Client shutting down...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
