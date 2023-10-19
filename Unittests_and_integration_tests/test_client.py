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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """
        Test public_repos method
        """
        mock_payload = [
            {
                "name": "episodes.dart",
                "license": {
                    "key": "bsd-3-clause",
                    "name": "BSD 3-Clause \"New\" or \"Revised\" License",
                    "spdx_id": "BSD-3-Clause",
                    "url": "https://api.github.com/licenses/bsd-3-clause",
                    "node_id": "MDc6TGljZW5zZTU="
                },
            },
            {
                "name": "cpp-netlib",
                "license": {
                    "key": "bsl-1.0",
                    "name": "Boost Software License 1.0",
                    "spdx_id": "BSL-1.0",
                    "url": "https://api.github.com/licenses/bsl-1.0",
                    "node_id": "MDc6TGljZW5zZTI4"
                },
            }
        ]
        mock_get_json.return_value = mock_payload

        test_class = GithubOrgClient("google")

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_url:

            mock_url.return_value = "https://api.github.com/orgs/google/repos"
            self.assertEqual(test_class.public_repos(
                license="bsd-3-clause"), ["episodes.dart"])

            self.assertEqual(test_class.public_repos(
                license="bsl-1.0"), ["cpp-netlib"])

            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/google/repos")

            mock_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_output):
        """
        Test has_license method
        """
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected_output)
