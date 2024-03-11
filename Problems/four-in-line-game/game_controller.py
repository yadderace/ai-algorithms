import socket
import threading
import random
import string

class GameServer:
    def __init__(self, host='127.0.0.1', port=5555):
        """
        Initialize the GameServer object with the host and port.

        Args:
            host (str): Host address for the server.
            port (int): Port number for the server.
        """
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients_waiting = []

    def generate_client_code(self):
        """
        Generate a random 6-character code.

        Returns:
            str: Randomly generated code.
        """
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    def handle_client(self, client_socket, client_address):
        """
        Handle client connections and manage the waiting list of clients.

        Args:
            client_socket (socket.socket): Client socket object.
            client_address (tuple): Client address (host, port).
        """
        unique_code = self.generate_client_code()
        print(f"Connection from {client_address}. Sending unique code: {unique_code}")
        client_socket.sendall(unique_code.encode())
        
        client_socket.sendall(b"Do you want to connect with another client? (Y/N): ")
        response = client_socket.recv(1024).decode().strip().upper()

        if response == 'Y':
            client_socket.sendall(b"OK, waiting for another player to connect...")
            self.clients_waiting.append(client_socket)
            
            if len(self.clients_waiting) == 2:
                self.start_game(self.clients_waiting.pop(), self.clients_waiting.pop())
        else:
            client_socket.sendall(b"OK, maybe next time!")
        
        client_socket.close()

    def start_game(self, client1_socket, client2_socket):
        """
        Start a game between two clients.

        Args:
            client1_socket (socket.socket): Client 1 socket object.
            client2_socket (socket.socket): Client 2 socket object.
        """
        client1_socket.sendall(b"Game is starting! You are Player 1.")
        client2_socket.sendall(b"Game is starting! You are Player 2.")

    def start_server(self):
        """
        Start the server and listen for incoming connections.
        """
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")

        try:
            while True:
                client_socket, client_address = self.server_socket.accept()
                print(f"New connection from {client_address}")

                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_address))
                client_thread.start()
        except KeyboardInterrupt:
            print("Server interrupted. Closing connections.")
            self.server_socket.close()

if __name__ == "__main__":
    game_server = GameServer()
    game_server.start_server()