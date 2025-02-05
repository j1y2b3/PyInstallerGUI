import os
import unittest

from data import root
from data import getIconPath, getRecentFiles, writeRecentFiles


class TestData(unittest.TestCase):

    def test_get_icon_path(self):
        
        self.assertTrue(os.path.exists(getIconPath()))
        self.assertTrue(os.path.exists(getIconPath("console")))
        self.assertTrue(os.path.exists(getIconPath("windowed")))
        self.assertRaisesRegex(ValueError, 'style must be "console" or "windowed"',
                               getIconPath, 'other')
    
    def test_get_and_write_recent_files(self):

        jsonfile = 'temp.json'
        recentfiles = ['c', 'a', 'b']

        self.assertEqual(getRecentFiles(jsonfile), [])
        writeRecentFiles(recentfiles, jsonfile)
        self.assertEqual(getRecentFiles(jsonfile), recentfiles)
        self.assertEqual(getRecentFiles(jsonfile)[0], recentfiles[0])
        os.remove(os.path.join(root, jsonfile))
