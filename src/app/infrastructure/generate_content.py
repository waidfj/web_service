from src.app.consts.file_types import FILE_TYPES


def generate_content(filename, filepath, filetype):
    if filetype == FILE_TYPES.DOCUMENT:
        # get html file
        fin = open(filepath, 'r', encoding='utf-8')
        body = fin.read().encode('utf-8')
        content_type = 'text/html; charset=utf-8'

    elif filetype == FILE_TYPES.IMAGE:
        # get image file
        fin = open(filepath, 'rb')
        body = fin.read()
        ext = filename.split('.')[-1]
        content_type = f'image/{ext}' if ext != 'ico' else 'image/x-icon'
    
    return body, content_type
