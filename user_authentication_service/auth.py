#!/usr/bin/env python3
""" module to create Hash password
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Generate a salted hash of the input password using bcrypt

    Args:
    password (str): The password to hash

    Returns (byte): The hashed password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)

    return hashed
