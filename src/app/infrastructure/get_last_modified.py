from email.utils import formatdate
import os
from src.app.consts.server_env import FILES_PATH


def get_last_modified(filepath):
    mtime = os.path.getmtime(filepath)
    
    return formatdate(mtime, usegmt=True)
