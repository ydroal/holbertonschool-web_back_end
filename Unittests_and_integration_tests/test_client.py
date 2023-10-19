#!/usr/bin/env python3
"""
Test module
"""
import unittest
from unittest.mock import patch
from unittest.mock import PropertyMock
from utils import memoize
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for client module
    """
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get):
        """
        Test org method
        """
        test_class = GithubOrgClient(org_name)
        mock_get.return_value = (
            test_class.ORG_URL.format(org=test_class._org_name)
            )
        self.assertEqual(test_class.org, mock_get.return_value)
        mock_get.assert_called_once_with(
            test_class.ORG_URL.format(org=test_class._org_name))

    def test_public_repos_url(self):
        """
        Test _public_repos_url method
        """

        test_class = GithubOrgClient("google")
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_payload = {
                "repos_url": "https://api.github.com/orgs/google/repos"
                }
            mock_org.return_value = mock_payload

            self.assertEqual(test_class._public_repos_url,
                             "https://api.github.com/orgs/google/repos")
            mock_org.assert_called_once()
