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

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)

class TestGetJson(TestCase):
    """ Class for testing get_json function """
    # order of args: test_url, test_payload
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test method returns correct output """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)
            mock_response.json.assert_called_once()

class TestMemoize(TestCase):
    """ Class for testing memoization """

    def test_memoize(self):
        """ Tests memoize function """

        class TestClass:
            """ Test class """

            def a_method(self):
                """ Method to always return 42 """
                return 42

            @memoize
            def a_property(self):
                """ Returns memoized property """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)
            patched.assert_called_once()
