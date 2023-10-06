#!/usr/bin/env python3
""" Module to manage the API authentication
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    '''Define BasicAuth class'''

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        '''
        Args:
        authorization_header (str): value of the header request Authorization

        Returns:
        str: the Base64 part of the Authorization header
        '''

        if not authorization_header:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        return authorization_header[6:]
