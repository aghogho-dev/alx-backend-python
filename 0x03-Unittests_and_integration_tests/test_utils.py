#!/usr/bin/env python3
"""Module to test utils.py"""

from parameterized import parameterized
import requests
import unittest
from unittest.mock import patch
from utils import access_nested_map
from utils import get_json
from utils import memoize


class TestAcessNestedMap(unittest.TestCase):
    """Nested Map Class"""

    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_acess_nested_map(self, nested_map, path, expected):
        """Test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), "b")
    ])

    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access nested map exception"""
        with self.assertRaises(KeyError) as exc:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(exc.exception))

