#!/usr/bin/env python3
"""
Test module
"""
import unittest
from parameterized import parameterized
import utils


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
        self.assertEqual(utils.access_nested_map(nested_map, path), expected_output)