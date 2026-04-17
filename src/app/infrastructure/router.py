from src.app.application.generate_forbidden import generate_forbidden
from src.app.application.generate_not_modified import generate_not_modified
from src.app.application.generate_not_found import generate_not_found
from src.app.application.generate_bad_request import generate_bad_request
from src.app.application.generate_ok import generate_ok
from src.app.consts.file_types import FILE_TYPES
from src.app.consts.header_names import CONNECTION, CONNECTION_HEADER, \
    IF_MODIFIED_SINCE_HEADER, SEC_FETCH_DEST_HEADER
from src.app.consts.server_env import FILES_PATH, HOME, PRIVATE_FOLDER
from src.app.infrastructure.generate_content import generate_content
from src.app.infrastructure.get_last_modified import get_last_modified


# Handles the request
def route(request_line, headers):
    # Determin connection type (persistent/non-persistent)
    connection = headers[CONNECTION_HEADER] if CONNECTION_HEADER in headers \
        else CONNECTION.PERSISTENT

	# validate if bad request
    if request_line[0] != 'GET' or SEC_FETCH_DEST_HEADER not in headers:
        return generate_bad_request(connection)

    file_type = headers[SEC_FETCH_DEST_HEADER]
    if file_type not in FILE_TYPES.values():
        return generate_bad_request(connection)

    # extract the file name & path
    filename = HOME if request_line[1] == '/' else request_line[1]
    filepath = FILES_PATH + filename

    # Verify if file exists & calculate last_modified
    try :
        last_modified = get_last_modified(filepath)
    except FileNotFoundError:
        return generate_not_found(connection)

    # Verify if file is forbidden
    if PRIVATE_FOLDER in filepath.split('/'):
        return generate_forbidden(connection)

    # Check if file is modified
    if IF_MODIFIED_SINCE_HEADER in headers \
        and last_modified == headers[IF_MODIFIED_SINCE_HEADER].strip():
            return generate_not_modified(connection, last_modified)

    # Generate the response body
    body, content_type = generate_content(filename, filepath, file_type)

    return generate_ok(body, connection, last_modified, content_type)
