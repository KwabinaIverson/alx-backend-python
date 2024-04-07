#!/usr/bin/python3
"""A unittest that checks a method works as intended."""
from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """
    A test case class for the access_nested_map function.

    This class tests the behavior of the access_nested_map
    function with different inputs.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nest_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function with various inputs.

        Arguments:
            - nested_map: A dictionary representing the nested map.
            - path: A tuple representing the path to access
                the value in the nested map.
            - expected_result: The expected result after
                accessing the nested value.

        This method tests the access_nested_map function by providing
        different nested maps and paths.
        It compares the result obtained from the function
        with the expected result.
        """
        actual_output = access_nested_map(nested_map, path)
        self.assertEqual(actual_output, expected_result)
