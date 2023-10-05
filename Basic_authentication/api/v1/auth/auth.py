#!/usr/bin/env python3
""" Module to manage the API authentication
"""
from flask import request
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
        bool: False
        '''
        return False

    def authorization_header(self, request=None) -> str:
        '''
        Args:
        request (Optional[Request]): Flask request object

        Returns:
        str: None
        '''
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''
        Args:
        rrequest (Optional[Request]): Flask request object.

        Returns:
        User: None
        '''
        return None
