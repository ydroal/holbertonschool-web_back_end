#!/usr/bin/env python3
""" Module to manage the API authentication
"""
import uuid
from api.v1.auth.auth import Auth
from models.user import User


class SessionAuth(Auth):
    '''Define SessionAuth class'''

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''
        Creates a Session ID for a user_id

        Args:
        user_id (str): user id

        Returns:
        str: session id
        '''
        if not user_id:
            return None
        if not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''
        Returns a User ID based on a Session ID

        Args:
        session_id (str): session ID

        Returns:
        str: User ID
        '''
        if not session_id:
            return None
        if not isinstance(session_id, str):
            return None

        user_id = self.user_id_by_session_id.get(session_id)

        return user_id

    def current_user(self, request=None):
        '''
        Returns a User instance based on a cookie value

        Args:
        request: Flask request object

        Returns:
        User: User instance
        '''

        session_id = self.session_cookie(request)
        if not session_id:
            return None

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return None

        return User.get(user_id)

    def destroy_session(self, request=None):
        '''
        Deletes the user session / logout:

        Args:
        request: Flask request object

        Returns:
        bool: True if the session is successfully destroyed, False otherwise.
        '''

        if not request:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        self.user_id_by_session_id.pop(session_id, False)

        return True
