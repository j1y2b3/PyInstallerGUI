import unittest

from gui import Win


class TestGUI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.win = Win()

    def test_win(self):
        
        self.win.win.after(1000, self.win.close)
        self.win.run()