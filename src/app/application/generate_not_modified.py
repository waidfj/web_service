from src.app.application.generate_response import generate_response
from src.app.consts.http_response import RESPONSE_LINE


# Returns a 304 Not Modified response formatted
def generate_not_modified(connection, last_modified):
    return generate_response(RESPONSE_LINE.NOT_MODIFIED, ''.encode('utf-8'), connection, last_modified, None)
