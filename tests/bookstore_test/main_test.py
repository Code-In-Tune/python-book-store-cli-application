import unittest
from bookstore import main


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here
        main.print_hi("Hello")




if __name__ == '__main__':
    unittest.main()
