from src.app.application.generate_response import generate_response
from src.app.consts.http_response import RESPONSE_LINE


def generate_forbidden(connection):
    body = '<h1>\
        Forbidden, you do not have permission to access this resource\
            </h1>'.encode('utf-8')

    return generate_response(RESPONSE_LINE.FORBIDDEN, body, connection, None, 'text/html')
