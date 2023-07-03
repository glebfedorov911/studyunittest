import unittest
from prog import split_string

class TestSplitString(unittest.TestCase):

    def test_func(self):
        self.assertEqual(split_string("equal equal"), "equal equal".split(' '))
        self.assertEqual(split_string("equal equal fdk skjf ksdfjksdf"), "equal equal fdk skjf ksdfjksdf".split(' '))
        self.assertEqual(split_string("equal"), "equal".split(' '))
        self.assertEqual(split_string(" "), " ".split(' '))
        self.assertEqual(split_string(""), "".split(' '))

    def test_type(self):
        self.assertRaises(TypeError, split_string, [1, 2, 3])
        self.assertRaises(TypeError, split_string, 12341412)
        self.assertRaises(TypeError, split_string, True)