import os
import unittest

from data import root
from data import getIconPath, getRecentPaths, writeRecentPaths


class TestData(unittest.TestCase):

    def test_get_icon_path(self):
        
        self.assertTrue(os.path.exists(getIconPath()))
        self.assertTrue(os.path.exists(getIconPath("console")))
        self.assertTrue(os.path.exists(getIconPath("windowed")))
        self.assertRaisesRegex(ValueError, 'style must be "console" or "windowed"',
                               getIconPath, 'other')
    
    def test_get_and_write_recent_paths(self):

        file = 'temp.json'
        paths = ('a', 'b')

        self.assertEqual(getRecentPaths(file), ())
        writeRecentPaths(paths, file)
        self.assertEqual(getRecentPaths(file), paths)
        os.remove(os.path.join(root, file))        
