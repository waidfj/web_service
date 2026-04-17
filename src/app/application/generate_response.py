from src.app.consts.header_names import CONNECTION_HEADER, CONTENT_LENGTH_HEADER, \
    CONTENT_TYPE_HEADER, HEADER_SEPARATOR, LAST_MODIFIED_HEADER


# Formats the response to match HTTP format
def generate_response(response_line, body, connection, last_modified, content_type):
    # Last-Modified and Content-Type are optional (they don't exist in no content responses)
    if last_modified:
        last_modified = LAST_MODIFIED_HEADER + f': {last_modified}' + HEADER_SEPARATOR
    else:
        last_modified = ''

    if content_type:
        content_type = CONTENT_TYPE_HEADER + f': {content_type}' + HEADER_SEPARATOR
    else:
        content_type = ''

    return (
        response_line +
        CONTENT_LENGTH_HEADER + f': {len(body)}' + HEADER_SEPARATOR +
        content_type +
        last_modified +
        CONNECTION_HEADER + f': {connection}' + HEADER_SEPARATOR +
        HEADER_SEPARATOR
    ).encode('ascii') + body
