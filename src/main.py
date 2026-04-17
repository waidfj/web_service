import socket
import threading

from src.app.consts.server_env import SERVER_HOST, SERVER_PORT
from src.app.infrastructure.handle_connection import handle_connection


# Start connections and dedicate a thread for each
def run_server():
	# Create a TCP socket & set the server to listen
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((SERVER_HOST, SERVER_PORT))
	server_socket.listen(1)

	# Accept connections and create threads to handle them
	while True:
		client_connection, client_address = server_socket.accept()

		client_thread = threading.Thread(target=handle_connection, args=(client_connection,))
		client_thread.start()
