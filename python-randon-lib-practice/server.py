import socket


def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 12345

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    # Establish a connection
    client_socket, addr = server_socket.accept()
    print(f"Got a connection from {addr}")

    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('ascii')
        print(f"Client: {message}")
        if message.lower() == 'bye':
            print("Client disconnected.")
            break

        # Send message to client
        response = input("Server: ")
        client_socket.send(response.encode('ascii'))
        if response.lower() == 'bye':
            print("Server disconnected.")
            break

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
