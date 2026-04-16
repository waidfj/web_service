from src.app.application.generate_response import generate_response
from src.app.consts.http_response import RESPONSE_LINE


def generate_bad_request(connection):
    body = '<h1>\
        Bad Request, major headers are missing or request type is not supported\
            </h1>'.encode('utf-8')

    return generate_response(RESPONSE_LINE.BAD_REQUEST, body, connection, None, 'text/html')
