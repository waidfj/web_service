from src.app.services.dict import MapDict

HEADER_SEPARATOR = '\r\n'

CONNECTION_HEADER = 'Connection'
CONNECTION = MapDict({
    'NONPERSISTENT_CONNECTION': 'close', 'PERSISTENT_CONNECTION': 'keep-alive'
})
