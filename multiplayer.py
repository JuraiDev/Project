import socket
import threading
import json






class MultiplayerManager:
    def __init__(self):
        self.server = None
        self.client = None
        self.game_state = {}

    def update(self):
        # Logic to update multiplayer state
        pass

    def handle_player_input(self, player_input):
        if player_input == "start_server":
            self.start_server()
        elif player_input.startswith("connect "):
            host, port = player_input.split()[1:]
            self.connect_to_server(host, int(port))
        elif self.client:
            self.client.send_data({"command": player_input})

    def start_multiplayer(self):
        choice = input("Do you want to host or join a game? (host/join): ")
        if choice == "host":
            self.server = GameServer()
            self.server.start_server('localhost', 5555)
        elif choice == "join":
            self.client = GameClient()
            self.client.connect_to_server('localhost', 5555)

class GameServer:
    def __init__(self):
        self.connections = []
        self.game_state = {}

    def start_server(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        print("Server started, waiting for connections...")
        while True:
            conn, addr = self.server_socket.accept()
            self.connections.append(conn)
            threading.Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn):
        while True:
            try:
                data = conn.recv(1024)
                if data:
                    received_state = json.loads(data.decode('utf-8'))
                    self.game_state.update(received_state)
                    self.broadcast_game_state(self.game_state)
            except:
                self.connections.remove(conn)
                conn.close()
                break

    def broadcast_game_state(self, game_state):
        for conn in self.connections:
            conn.send(json.dumps(game_state).encode('utf-8'))

class GameClient:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.game_state = {}

    def connect_to_server(self, host, port):
        self.client_socket.connect((host, port))
        threading.Thread(target=self.receive_data).start()

    def send_data(self, data):
        self.client_socket.send(json.dumps(data).encode('utf-8'))

    def receive_data(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                if data:
                    received_state = json.loads(data.decode('utf-8'))
                    self.game_state.update(received_state)
            except:
                self.client_socket.close()
                break

if __name__ == "__main__":
    module_updater = ModuleUpdater()
    module_updater.start_multiplayer()
    while True:
        player_input = input("Enter your command: ")
        module_updater.handle_player_input(player_input)
