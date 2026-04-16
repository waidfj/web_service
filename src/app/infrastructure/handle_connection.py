from src.app.consts.header_names import CONNECTION_HEADER, CONNECTION, HEADER_SEPARATOR
from src.app.infrastructure.router import route


def handle_connection(client_connection):
	while True:
		request = client_connection.recv(1024).decode()
		if not request:
			break

		lines = request.split(HEADER_SEPARATOR+HEADER_SEPARATOR, 1)[0].split(HEADER_SEPARATOR)
		headers = extractHeadersDictionary(lines)

		response = route(lines[0].split(), headers)
		client_connection.sendall(response)
		print(request)
		print(response.decode())

		if CONNECTION_HEADER not in headers \
			or headers[CONNECTION_HEADER] == CONNECTION.NON_PERSISTENT:
			break

	client_connection.close()


def extractHeadersDictionary(lines):
	headers = {}

	for line in lines[1:]:
		if ": " in line:
			key, value = line.split(": ", 1)
			headers[key] = value

	return headers