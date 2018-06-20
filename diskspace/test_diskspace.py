
import unittest

from diskspace import *

class TestDiskSpace(unittest.TestCase):
    
    def test(self):
        self.assertTrue(True)

    def test_upper(self):
        self.assertEqual(self.subprocess_check_output(), '')


if __name__ == '__main__':
    unittest.main()