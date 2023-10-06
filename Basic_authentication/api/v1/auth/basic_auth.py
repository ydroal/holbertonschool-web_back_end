#!/usr/bin/env python3
""" Module to manage the API authentication
"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth
from models.user import User


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        '''
        Args:
        base64_authorization_header (str): Base64 part of the Auth header

        Returns:
        str: decoded value of a Base64 of base64_authorization_header
        '''

        if not base64_authorization_header:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        # Base64のデコード時に無効なBase64文字列が渡されるとbinascii.Errorを発生させる
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        '''
        Args:
        decoded_base64_authorization_header (str): Base64 decoded value

        Returns:
        Tuple[str, str]: user email and password from the Base64 decoded value
        '''

        if not decoded_base64_authorization_header:
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        auth_data = decoded_base64_authorization_header.split(':')
        return (auth_data[0], auth_data[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        '''
        Args:
        user_email (str): Base64 decoded value
        user_pwd (str): Base64 decoded value

        Returns:
        User: User instance
        '''

        if user_email is None or not isinstance(user_email, str):
            return (None)

        if user_pwd is None or not isinstance(user_pwd, str):
            return (None)

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Overloads Auth and retrieves the User instance for a request

        Args:
        request: Flask request object

        Returns:
        User: User instance
        '''

        auth_header = self.authorization_header(request)
        if not auth_header:
            return None

        base64_auth_header = self.extract_base64_authorization_header(
                auth_header)
        if not base64_auth_header:
            return None

        decode_auth_header = self.decode_base64_authorization_header(
                base64_auth_header)
        if not decode_auth_header:
            return None

        user_email, user_pwd = self.extract_user_credentials(
                decode_auth_header)
        if not user_email or not user_pwd:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
