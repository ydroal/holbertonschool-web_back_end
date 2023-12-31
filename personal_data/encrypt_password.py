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


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''
    validate that the provided password matches the hashed password

    Args:
        hashed_password (bytes): hashed password
        password (str): provided password to validate

    Returns:
        bool: True if the password is valid, False otherwise
    '''
    return bcrypt.checkpw(password.encode(), hashed_password)
