from src.app.consts.header_names import CONNECTION_HEADER, CONTENT_LENGTH_HEADER, \
    CONTENT_TYPE_HEADER, HEADER_SEPARATOR, LAST_MODIFIED_HEADER


def generate_response(response_line, body, connection, last_modified, content_type):
    if last_modified:
        last_modified = LAST_MODIFIED_HEADER + f': {last_modified}' + HEADER_SEPARATOR
    else:
        last_modified = ''

    return (
        response_line +
        CONTENT_LENGTH_HEADER + f': {len(body)}' + HEADER_SEPARATOR +
        CONTENT_TYPE_HEADER + f': {content_type}' + HEADER_SEPARATOR +
        last_modified +
        CONNECTION_HEADER + f': {connection}' + HEADER_SEPARATOR +
        HEADER_SEPARATOR
    ).encode('ascii') + f'{body}'.encode('utf-8')
