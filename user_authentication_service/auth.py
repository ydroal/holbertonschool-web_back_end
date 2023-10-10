#!/usr/bin/env python3
""" Define Auth class
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
import uuid
from db import DB
from user import User


def _hash_password(password: str) -> str:
    """
    Generate a salted hash of the input password using bcrypt

    Args:
    password (str): The password to hash

    Returns (byte): The hashed password
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)

    return hashed.decode('utf-8')


def _generate_uuid() -> str:
    """
    Generate a string representation of a new UUID

    Returns (str): A new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a user in the database.

        Args:
        email (str): The email of the user to register
        password (str): The password of the user to register

        Returns: The User object of the registered
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists.')
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)

            return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate login credentials

        Args:
        email (str): The email of user
        password (str): The password provided

        Returns:
        True if the password matches the stored hashed password for the email
        False otherwise
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password.encode('utf-8'),
                              user.hashed_password.encode('utf-8'))
