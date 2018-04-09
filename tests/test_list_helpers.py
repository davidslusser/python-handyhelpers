# import system modules
import unittest

# import handyhelpers
import __init__
from handyhelpers.list_helpers import *


class TestListHelpers(unittest.TestCase):
    """ Execute unittests on handyhelpers/list_helpers.py """

    def test_slice_list_with_remainder(self):
        """ verify slice_list return equal slices of a list and includes expected remainder """
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        resp = slice_list(test_list, 4)
        self.assertIsInstance(resp, list)
        self.assertEquals(len(resp), 3)
        self.assertEquals(len(resp[-1]), 2)

    def test_slice_list_without_remainder(self):
        """ verify slice_list return equal slices of a list and excludes remainder """
        test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        resp = slice_list(test_list, 4, False)
        self.assertIsInstance(resp, list)
        self.assertEquals(len(resp), 2)

    def test_flatten_lists(self):
        """ verify multiple lists can be combined into a single list """
        resp = flatten_lists([1, 2], [1, 2, 3], [1, 2, 3, 4])
        self.assertIsInstance(resp, list)
        self.assertEquals(len(resp), 9)

    def test_flatten_lists_unique(self):
        """ verify multiple lists can be combined into a single list with unique elements """
        resp = flatten_lists_unique([1, 2], [1, 2, 3], [1, 2, 3, 4])
        self.assertIsInstance(resp, list)
        self.assertEquals(len(resp), 4)

    def test_flatten_lists_common(self):
        """ verify common elements of multiple lists can be combined into a single list with unique elements """
        resp = flatten_lists_common([1, 2], [1, 2, 3], [1, 2, 3, 4])
        self.assertIsInstance(resp, list)
        self.assertEquals(len(resp), 2)

    def test_reverse_nested_single(self):
        """ verify nested lists can be reversed """
        test_list = [1, 2, 3, 4]
        resp = reverse_nested(test_list)
        self.assertIsInstance(resp, list)
        self.assertEquals(resp, [4, 3, 2, 1])
        self.assertEquals(reverse_nested([[1, 2, 3, 4], [5, 6]]), [[6, 5], [4, 3, 2, 1]])

    def test_reverse_nested_multiple(self):
        """ verify nested lists can be reversed """
        test_list = [[1, 2, 3, 4], [5, 6]]
        resp = reverse_nested(test_list)
        self.assertIsInstance(resp, list)
        self.assertEquals(resp, [[6, 5], [4, 3, 2, 1]])

    def test_longest_length(self):
        """ verify length of longest list """
        test_list = [[1, 2, 3, 4], [5, 6]]
        resp = get_longest_length(test_list)
        self.assertIsInstance(resp, int)
        self.assertEquals(resp, 4)

    def test_shortest_length(self):
        """ verify length of shortest list """
        test_list = [[1, 2, 3, 4], [5, 6]]
        resp = get_shortest_length(test_list)
        self.assertIsInstance(resp, int)
        self.assertEquals(resp, 2)

    def test_x_elements(self):
        """ verify list of x elements from list of list """
        test_list = [[1, 2, 3, 4], [5, 6]]
        resp = get_x_elements(test_list, 1)
        self.assertIsInstance(resp, list)
        self.assertEquals(resp, [2, 6])

    def test_is_list_type(self):
        """ verify true of all list elements are the same type """
        test_list = [1, 2, 3, 4]
        resp = is_list_type(test_list, int)
        self.assertIsInstance(resp, bool)
        self.assertTrue(resp)
        test_list = [1, 2, "a", "b"]
        resp = is_list_type(test_list, int)
        self.assertFalse(resp)

    def test_is_consecutive(self):
        """ verify true if all list elements are consecutive """
        test_list = [1, 2, 3, 4]
        resp = is_consecutive(test_list)
        self.assertIsInstance(resp, bool)
        self.assertTrue(resp)
        test_list = [1, 9, 3, 5]
        resp = is_consecutive(test_list)
        self.assertFalse(resp)

    def test_is_consecutive_step(self):
        """ verify true if all list elements are consecutive """
        test_list = [1, 3, 5]
        resp = is_consecutive(test_list, step=2)
        self.assertIsInstance(resp, bool)
        self.assertTrue(resp)
        test_list = [1, 9, 3, 5]
        resp = is_consecutive(test_list, step=2)
        self.assertFalse(resp)


if __name__ == '__main__':
    unittest.main()
