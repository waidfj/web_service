from src.app.consts.server_env import LOG_FILE
from src.app.services.logger import log
from src.app.consts.header_names import CONNECTION_HEADER, CONNECTION, HEADER_SEPARATOR
from src.app.infrastructure.router import route


# Handles requests of a single client connection
def handle_connection(client_connection):
	while True:
		# Read request
		request = client_connection.recv(1024).decode()
		if not request:
			break

		# Log request
		log(LOG_FILE, request)

		# Generate & send response
		lines = request.split(HEADER_SEPARATOR+HEADER_SEPARATOR, 1)[0].split(HEADER_SEPARATOR)
		headers = extractHeadersDictionary(lines)

		response = route(lines[0].split(), headers)
		client_connection.sendall(response)

		# Log response
		log(LOG_FILE, response)
		log(LOG_FILE, "--------------------")

		# If connection is non-persistent close the connection
		if CONNECTION_HEADER in headers and headers[CONNECTION_HEADER] == CONNECTION.NON_PERSISTENT:
			break

	client_connection.close()


# Extracts the headers of the request to be accessed as a dictionary data-structure
def extractHeadersDictionary(lines):
	headers = {}

	for line in lines[1:]:
		if ": " in line:
			key, value = line.split(": ", 1)
			headers[key] = value

	return headers