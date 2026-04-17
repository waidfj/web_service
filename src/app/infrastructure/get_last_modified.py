from email.utils import formatdate
import os


# Calculates last_modified for an existing file, if file doesn't exist it throws FileNotFound exception
def get_last_modified(filepath):
    mtime = os.path.getmtime(filepath)
    
    return formatdate(mtime, usegmt=True)
