import os
import json

from .settings import (PROTECT_STATUS_FILE, PROTECT_STATUS_VARIABLE,
                       PROTECT_STATUS_DEFAULT, DIR_NAME)

STATUS_FILE_NAME = DIR_NAME + PROTECT_STATUS_FILE


def save_status(status):
    """Save current status to file"""
    try:
        f = open(STATUS_FILE_NAME, 'w')
        f.write(json.dumps({
            'status': status
        }))
        f.close()
    except (NameError, FileNotFoundError):
        pass


def get_status():
    """Get status from file"""
    try:
        f = open(STATUS_FILE_NAME, 'r')
        data = f.read()
        f.close()
        res = json.loads(data)['status']
    except (NameError, FileNotFoundError):
        save_status(PROTECT_STATUS_DEFAULT)
        res = (PROTECT_STATUS_DEFAULT)
    return str(res)
