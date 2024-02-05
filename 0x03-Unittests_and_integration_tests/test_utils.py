#!/usr/bin/env python3

""" Test utilities for github org client."""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock

from utils import (
    access_nested_map,
    get_json,
    memoize,
)

from typing import (
    Dict,
    Tuple,
    Union,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a", "b"], 2),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union(Dict, int)
                               ) -> None:
        """Test access_nested_map function."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         expected: Exception
                                         ) -> None:
        """Test access_nested_map function."""
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict
                      ) -> None:
        """Test get_json function."""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = test_payload
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Test memoize decorator."""

    def test_memoize(self) -> None:
        """Test memoize decorator."""
        class TestClass:
            """Test class."""
            def a_method(self):
                """a method."""
                return 42

            @memoize
            def a_property(self):
                """a property."""
                return self.a_method()

        with patch.object(TestClass,
                          'a_method',
                          return_value=42
                          ) as mock_method:
            tc = TestClass()
            self.assertEqual(tc.a_property, 42)
            self.assertEqual(tc.a_property, 42)
            mock_method.assert_called_once()
