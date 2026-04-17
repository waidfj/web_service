from src.app.services.dict import MapDict


HEADER_SEPARATOR = '\r\n'

# Connection values
CONNECTION = MapDict({
    'NON_PERSISTENT': 'close', 'PERSISTENT': 'keep-alive'
})

# Names of HTTP headers
CONNECTION_HEADER = 'Connection'
IF_MODIFIED_SINCE_HEADER = 'If-Modified-Since'
LAST_MODIFIED_HEADER = 'Last-Modified'
CONTENT_TYPE_HEADER = 'Content-Type'
CONTENT_LENGTH_HEADER = 'Content-Length'
SEC_FETCH_DEST_HEADER = 'Sec-Fetch-Dest'
