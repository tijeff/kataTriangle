from Triangle import Triangle
import unittest


class MyTestCase(unittest.TestCase):
    def test_print_triangle(self):
        triangle_under_test = Triangle(3, 6, 5)
        self.assertEqual("Triangle sides length: 3, 5, 6", str(triangle_under_test))

    def test_equilateral(self):
        triangle_under_test = Triangle(5, 5, 5)
        self.assertEqual("Triangle sides length: 5, 5, 5 is equilateral", str(triangle_under_test))

if __name__ == '__main__':
    unittest.main()
