import socket
import sys

def main():
    if len(sys.argv) != 5:
        print("Usage: python client.py <server_ip> <server_port> <PUBLISHER/SUBSCRIBER> <TOPIC>")
        sys.exit(1)

    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client_type = sys.argv[3].upper()
    topic = sys.argv[4]

    if client_type not in ("PUBLISHER", "SUBSCRIBER"):
        print("Invalid client type. Use PUBLISHER or SUBSCRIBER.")
        sys.exit(1)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((server_ip, server_port))
        client_socket.sendall(f"{client_type} {topic}".encode())

        if client_type == "PUBLISHER":
            print(f"You are in PUBLISHER mode for topic '{topic}'. Type 'terminate' to quit.")
            while True:
                message = input()
                if message.lower() == "terminate":
                    break
                client_socket.sendall(message.encode())
        else:
            print(f"You are in SUBSCRIBER mode for topic '{topic}'. Type 'terminate' to quit.")
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
