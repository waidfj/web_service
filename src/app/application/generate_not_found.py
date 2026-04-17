from src.app.application.generate_response import generate_response
from src.app.consts.http_response import RESPONSE_LINE


# Returns a 404 Not Found response formatted
def generate_not_found(connection):
    body = '<h1>Not Found</h1>'.encode('utf-8')

    return generate_response(RESPONSE_LINE.NOT_FOUND, body, connection, None, 'text/html')
