def log(destination, message):
    if isinstance(message, bytes):
        message = message.decode('utf-8', errors='replace')

    file = open(destination, 'a', encoding='utf-8')
    file.write(message + '\n\n')

    file.close()

def clear_log(destination):
    with open(destination, 'w'):
        pass
