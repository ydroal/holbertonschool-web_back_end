#!/usr/bin/env python3
""" Module to manage the API authentication
"""
from flask import request
from os import getenv
from typing import List, TypeVar


User = TypeVar('User')


class Auth:
    '''Define Auth class'''

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''
        Args:
        path (str):
        excluded_paths (List[str]):

        Returns:
        bool: True if the path is not in the list of strings excluded_paths
        '''
        if path is None or not excluded_paths or excluded_paths is None:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(self, request=None) -> str:
        '''
        Args:
        request (Optional[Request]): Flask request object

        Returns:
        str: value of the header request Authorization
        '''
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Args:
        rrequest (Optional[Request]): Flask request object.

        Returns:
        User: None
        '''
        return None

    def session_cookie(self, request=None):
        '''
        Returns a cookie value from a request

        Args:
        request: Flask request object.

        Returns:
        str: cookie value
        '''
        if not request:
            return None

        cookie_name = getenv('SESSION_NAME')
        return request.cookies.get(cookie_name)
