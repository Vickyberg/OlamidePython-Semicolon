import unittest
import utils


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("I run only once")

    @classmethod
    def tearDown(self) -> None:
        print("runs after all")

    def test_something(self):
        self.assertEqual(True, True)

    def test_add(self):
        self.assertEqual(5, utils.add(3, 2))

    def test_list(self):
        self.assertEqual([1, 4, 9], utils.square_list([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
