#!/usr/bin/env python3
""" Module to manage the API authentication
"""
import base64
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
