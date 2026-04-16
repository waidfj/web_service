from src.app.application.generate_response import generate_response
from src.app.consts.http_response import RESPONSE_LINE


def generate_ok(body, connection, last_modified, content_type):
    return generate_response(RESPONSE_LINE.OK, body, connection, last_modified, content_type)
