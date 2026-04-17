import mimetypes
from src.app.consts.file_types import FILE_TYPES


# Creates the body of the reponse
def generate_content(filename, filepath, filetype):
    if filetype == FILE_TYPES.DOCUMENT:
        # get text file
        fin = open(filepath, 'r', encoding='utf-8')
        body = fin.read().encode('utf-8')

        #DECLARATION: This snippet is AI-Generated
        content_type, _ = mimetypes.guess_type(filename)
        if not content_type or not content_type.startswith('text/'):
            content_type = 'text/plain; charset=utf-8'
        elif 'charset' not in content_type:
            content_type += '; charset=utf-8'

    elif filetype == FILE_TYPES.IMAGE:
        # get image file
        fin = open(filepath, 'rb')
        body = fin.read()
        ext = filename.split('.')[-1]
        content_type = f'image/{ext}' if ext != 'ico' else 'image/x-icon'
    
    return body, content_type
