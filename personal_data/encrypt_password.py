#!/usr/bin/env python3
'''Module to return a salted, hashed password, which is a byte string'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''
    returns a salted, hashed password, which is a byte string.

    Args:
        password (str): password to be hashed

    Returns:
        bytes: the hashed password
    '''
    salt = bcrypt.gensalt()

    hashed = bcrypt.hashpw(password.encode(), salt)

    return hashed
