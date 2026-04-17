from src.app.consts.header_names import HEADER_SEPARATOR
from src.app.services.dict import MapDict


# Maps HTTP Status to the correct response line
RESPONSE_LINE = MapDict({
    'OK': f'HTTP/1.1 200 OK{HEADER_SEPARATOR}',
    'NOT_FOUND': f'HTTP/1.1 404 Not Found{HEADER_SEPARATOR}',
    'BAD_REQUEST': f'HTTP/1.1 400 Bad Request{HEADER_SEPARATOR}',
    'NOT_MODIFIED': f'HTTP/1.1 304 Not Modified{HEADER_SEPARATOR}',
    'FORBIDDEN': f'HTTP/1.1 403 Forbidden{HEADER_SEPARATOR}'
})
