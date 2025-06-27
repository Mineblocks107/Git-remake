import os

def pad_path(path: str, pad: str = 'pad') -> str:
    # Determine prefix (./, /, or empty)
    prefix = ''
    if path.startswith('./'):
        prefix = './'
        path = path[2:]
    elif path.startswith('/'):
        prefix = '/'
        path = path[1:]

    # Split the path and insert pad
    parts = path.split('/')
    padded_parts = []
    for part in parts:
        if part:  # skip empty parts
            padded_parts.extend([pad, part])

    return os.path.join(prefix, *padded_parts)