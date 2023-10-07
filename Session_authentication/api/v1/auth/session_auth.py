#!/usr/bin/env python3
""" Module to manage the API authentication
"""
import uuid
from api.v1.auth.auth import Auth


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
