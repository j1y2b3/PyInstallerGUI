import os
import unittest

from data import get_icon_path


class TestData(unittest.TestCase):

    def test_get_icon_path(self):
        
        self.assertTrue(os.path.exists(get_icon_path()))
        self.assertTrue(os.path.exists(get_icon_path("console")))
        self.assertTrue(os.path.exists(get_icon_path("windowed")))
        self.assertRaisesRegex(ValueError, 'style must be "console" or "windowed"',
                               get_icon_path, 'other')