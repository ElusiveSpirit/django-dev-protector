import os

from .settings import (PROTECT_STATUS_FILE, PROTECT_STATUS_VARIABLE,
                       PROTECT_STATUS_DEFAULT, DIR_NAME)

STATUS_FILE_NAME = DIR_NAME + PROTECT_STATUS_FILE


def save_to_file(text, file_name):
    try:
        f = open(file_name, 'w')
        f.write(str(text))
        f.close()
    except:
        pass


def get_from_file(file_name):
    """Gets first word from file"""
    try:
        f = open(file_name, 'r')
        data = f.read()
        f.close()

        import re
        data = re.findall('\w+', data)
        return data[0]
    except:
        return ''


def save_status(status):
    """Save current status to file"""
    save_to_file(status, STATUS_FILE_NAME)


def get_status():
    """Get status from file"""
    res = get_from_file(STATUS_FILE_NAME)
    if not res:
        save_status(PROTECT_STATUS_DEFAULT)
        return str(PROTECT_STATUS_DEFAULT)
    return res
