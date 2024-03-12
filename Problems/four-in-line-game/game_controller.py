import socket
import threading
import random
import string

from game import FourInLine

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
        print(f"Connection from {client_address}")

        # Ask the client for their preferred symbol
        player_symbol = self.get_player_symbol(client_socket)
        
        # Prompt the client with the choice to play alone or wait for another player
        client_socket.sendall(b"Do you want to play alone with the computer? (Y/N): ")
        response = client_socket.recv(1024).decode().strip().upper()

        if response == 'Y':
            client_socket.sendall(b"OK, playing alone with the computer...")
            # TODO: Implement logic to play against the computer (not implemented yet)
        else:
            client_socket.sendall(b"OK, waiting for another player...")
            # Add player's symbol and socket to the waiting list
            self.clients_waiting.append((client_socket, player_symbol))
            
            if len(self.clients_waiting) == 2:
                player1_socket, player1_symbol = self.clients_waiting.pop(0)
                player2_socket, player2_symbol = self.clients_waiting.pop(0)

                # Ensure the symbols are different
                while player1_symbol == player2_symbol:
                    player2_socket.sendall(b"Your symbol is the same as Player 1's. Choose another symbol: ")
                    player2_symbol = self.get_player_symbol(player2_socket)
                
                self.start_game(player1_socket, player1_symbol, player2_socket, player2_symbol)
        
        client_socket.close()

    def validate_move(self, game, player_socket, player_symbol, column):
        """
        Validate a player's move and update the game board if the move is valid.

        Args:
            game (FourInLine): Instance of the FourInLine game.
            player_socket (socket.socket): Player's socket object.
            player_symbol (str): Player's chosen symbol.

        Returns:
            bool: True if the move is valid and updated, False otherwise.
        """
        if game.make_move(column, player_symbol):  # If valid move
            player_board = game.get_board_string()
            player_socket.sendall(player_board.encode())
            return True
        else:
            player_socket.sendall(b"Invalid move. Please try again.")
            return False

    def check_winner(self, game, player_socket, player_symbol):
        """
        Check if a player has won the game.

        Args:
            game (FourInLine): Instance of the FourInLine game.
            player_socket (socket.socket): Player's socket object.
            player_symbol (str): Player's chosen symbol.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        if game.check_win(player_symbol):  # Check if the player wins
            player_socket.sendall(b"Congratulations! You win!")
            return True
        return False
    
    def ask_column(self, player_socket):
        """
        Prompt the player to enter the column number.

        Args:
            player_socket (socket.socket): Player's socket object.

        Returns:
            int: Column number entered by the player.
        """
        while True:
            player_socket.sendall(b"Your turn. Enter column number (1-7): ")
            column_input = player_socket.recv(1024).decode().strip()
            
            if not column_input.isdigit():
                player_socket.sendall(b"Invalid input. Please enter a number.\n")
                continue
            
            column = int(column_input) - 1
            
            if not (0 <= column < 7):
                player_socket.sendall(b"Invalid column number. Please enter a number between 1 and 7.\n")
                continue
            
            return column
    
    def get_player_symbol(self, player_socket):
        """
        Prompt the player to choose a symbol.

        Args:
            player_socket (socket.socket): Player's socket object.

        Returns:
            str: Player's chosen symbol.
        """
        while True:
            player_socket.sendall(b"Choose your symbol (1 character): ")
            symbol = player_socket.recv(1024).decode().strip()
            if len(symbol) == 1:
                return symbol
            else:
                player_socket.sendall(b"Invalid symbol. Please choose a single character.")

    def start_game(self, player1_socket, player1_symbol, player2_socket, player2_symbol):
        """
        Start a game between two clients.

        Args:
            player1_socket (socket.socket): Player 1 socket object.
            player1_symbol (str): Player 1's chosen symbol.
            player2_socket (socket.socket): Player 2 socket object.
            player2_symbol (str): Player 2's chosen symbol.
        """
        try:
            player1_socket.sendall(b"Game is starting! You are Player 1.")
            player2_socket.sendall(b"Game is starting! You are Player 2.")
        except OSError as e:
            print("Error occurred while sending data:", e)
            return

        # Initialize the FourInLine game
        game = FourInLine()

        while True:
            # Player 1's turn
            column = self.ask_column(player1_socket)
            if self.validate_move(game, player1_socket, player1_symbol, column):
                if self.check_winner(game, player1_socket, player1_symbol):
                    player2_socket.sendall(b"Sorry, you lose.")
                    break

            # Player 2's turn
            column = self.ask_column(player1_socket)
            if self.validate_move(game, player2_socket, player2_symbol, column):
                if self.check_winner(game, player2_socket, player2_symbol):
                    player1_socket.sendall(b"Sorry, you lose.")
                    break

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

# -------------------------------------------------------------------------------

def run_client():
    host = '127.0.0.1'  # Server's IP address
    port = 5555         # Server's port

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Receive the initial message from the server
        print(client_socket.recv(1024).decode())

        # Start communicating with the server
        while True:
            # Get user input and send it to the server
            user_input = input("Enter your message: ")
            client_socket.sendall(user_input.encode())

            # Receive and print the server's response
            response = client_socket.recv(1024).decode()
            print("Server:", response)

    except KeyboardInterrupt:
        print("Client closed.")
    finally:
        # Close the socket connection
        client_socket.close()

def main():
    choice = input("Do you want to run the client (C) or the server (S)? ").upper()

    if choice == "C":
        run_client()
    elif choice == "S":
        # Run the server code
        game_server = GameServer()
        game_server.start_server()
    else:
        print("Invalid choice. Please enter 'C' for client or 'S' for server.")

if __name__ == "__main__":
    main()