import socket


def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 12345

    # Connection to hostname on the port
    client_socket.connect((host, port))

    while True:
        # Send message to server
        message = input("Client: ")
        client_socket.send(message.encode('ascii'))
        if message.lower() == 'bye':
            print("Client disconnected.")
            break

        # Receive message from server
        response = client_socket.recv(1024).decode('ascii')
        print(f"Server: {response}")
        if response.lower() == 'bye':
            print("Server disconnected.")
            break

    client_socket.close()


if __name__ == "__main__":
    start_client()
