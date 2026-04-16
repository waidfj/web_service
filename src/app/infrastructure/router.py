from src.app.application import generate_not_modified
from src.app.application.generate_not_found import generate_not_found
from src.app.application.generate_bad_request import generate_bad_request
from src.app.application.generate_ok import generate_ok
from src.app.consts.file_types import FILE_TYPES
from src.app.consts.header_names import CONNECTION, CONNECTION_HEADER, \
    IF_MODIFIED_SINCE_HEADER, SEC_FETCH_DEST_HEADER
from src.app.consts.server_env import FILES_PATH
from src.app.infrastructure.generate_content import generate_content
from src.app.infrastructure.get_last_modified import get_last_modified


def route(request_line, headers):
    if CONNECTION_HEADER in headers:
        connection = headers[CONNECTION_HEADER]
    else:
        connection = CONNECTION.NON_PERSISTENT

	# validate if bad request
    if request_line[0] != 'GET' or SEC_FETCH_DEST_HEADER not in headers:
        if CONNECTION_HEADER in headers:
            return generate_bad_request(connection)
        return generate_bad_request(connection)

    file_type = headers[SEC_FETCH_DEST_HEADER]
    if file_type not in FILE_TYPES.values():
        return generate_bad_request(connection)

    # extract the file name
    filename = request_line[1]
    if filename == '/':
        filename = '/index.html'
    filepath = FILES_PATH + filename

    try :
        last_modified = get_last_modified(filepath)
    except FileNotFoundError:
        return generate_not_found(connection)
    
    if IF_MODIFIED_SINCE_HEADER in headers:
        if last_modified == headers[IF_MODIFIED_SINCE_HEADER].strip():
            return generate_not_modified(connection, last_modified)


    body, content_type = generate_content(filename, filepath, headers[SEC_FETCH_DEST_HEADER])

    return generate_ok(body, connection, last_modified, content_type)
