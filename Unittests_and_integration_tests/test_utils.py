#!/usr/bin/env python3
"""
Test module
"""
import unittest
from parameterized import parameterized
import requests
import utils
from utils import memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class for utils module
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        """
        Test access_nested_map method
        """
        self.assertEqual(utils.access_nested_map(nested_map, path),
                         expected_output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map method - case exception
        """
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test class for get_json()
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):  # Mockも引数に
        """
        Test get_json method - returns a Mock object
        """
        mock_get.return_value.json.return_value = test_payload  # Mockに戻り値設定
        self.assertEqual(utils.get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test class for memoization
    """

    def test_memoize(self):
        """
        Test memoize method
        """
        class TestClass:
            """
            Define Test class
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42)\
                as mock_a_method:

            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)

            mock_a_method.assert_called_once()
