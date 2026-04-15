from src.app.services.dict import MapDict


HEADER_SEPARATOR = '\r\n'

CONNECTION_HEADER = 'Connection'
CONNECTION = MapDict({
    'NON_PERSISTENT': 'close', 'PERSISTENT': 'keep-alive'
})

LAST_MODIFIED_HEADER = 'Last-Modified'
CONTENT_TYPE_HEADER = 'Content-Type'
CONTENT_LENGTH_HEADER = 'Content-Length'
SEC_FETCH_DEST_HEADER = 'Sec-Fetch-Dest'
