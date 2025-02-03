import unittest

from gui import Win
from gui import Required


class TestEachWidge(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.win = Win()
        cls.root = cls.win.root
        cls.root.title('Test Each Widge')
    
    @classmethod
    def tearDownClass(cls):

        cls.win.loop()
    
    def test_required(self):

        self.required = Required(self.root)
        self.required.place()

class TestAll(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.win = Win()
        cls.root = cls.win.root
        cls.root.title('Test All')

    @classmethod
    def tearDownClass(cls):

        cls.win.loop()
    
    def test_all(self):

        self.root.after(1000, self.win.close)
        self.win.show()
