import socket
import threading

from src.app.consts.server_env import SERVER_HOST, SERVER_PORT
from src.app.infrastructure import handle_connection

def run_server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind((SERVER_HOST, SERVER_PORT))
	server_socket.listen(1)

	while True:
		client_connection, client_address = server_socket.accept()

		client_thread = threading.Thread(target=handle_connection, args=(client_connection,))
		client_thread.start()
