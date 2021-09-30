# Taken from: http://code.activestate.com/recipes/173220-test-if-a-file-or-string-is-text-or-binary/

KNOWN_BINARY_FILE_EXTS = [
    ".pdf",
    ".pyc",
]


def is_textfile(filename, blocksize=512):
    """
    Tries to check if the given file is a text file.

    Exclude certain file extensions, such as PDF.

    :return {bool}: True if file is a text file else False
    """
    if any(filename.endswith(ext) for ext in KNOWN_BINARY_FILE_EXTS):
        return False
    return is_text(open(filename, "rb").read(blocksize))


def is_text(content):
    """
    Check if the provided content is text.

    :return {bool}: True if content is text else False
    """
    if b"\0" in content:
        return False
    if not content:  # Empty files are considered text
        return True
    # Try to decode as UTF-8
    try:
        content.decode("utf8")
    except UnicodeDecodeError:
        return False
    else:
        return True
