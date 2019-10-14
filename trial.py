import unittest

class Trying(unittest.TestCase):
    def setUp(self):
        print("Hello")

    def test_something(self):
        print("How are you guys doing")

    def tearDown(self):
        print("Have a nice day!")

if __name__ == "__main__":
    unittest.main()