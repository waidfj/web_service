from src.app.application.generate_bad_request import generate_bad_request
from src.app.consts.header_names import CONNECTION, CONNECTION_HEADER, SEC_FETCH_DEST_HEADER


def route(request_line, headers):
	# validate if bad request
        # return bad request
    if request_line[0] != 'GET' or SEC_FETCH_DEST_HEADER not in headers:
        if CONNECTION_HEADER in headers:
            return generate_bad_request(headers[CONNECTION_HEADER])
        return generate_bad_request(CONNECTION.NON_PERSISTENT)

    # extract the file name

    # if type is document
        # get last-modified for the file
        # handle 'if-modified' header
        # return the file
        # if the file not found, return 404 not found


    # if type is image
        # get last-modified for the file
        # handle 'if-modified' header
        # return the file
        # if the file not found, return 404 not found


    # if another type
        # return bad request
    pass
