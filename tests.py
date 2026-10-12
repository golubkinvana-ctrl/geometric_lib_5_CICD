import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle_area(0), 0)

    def test_area_positive(self):
        self.assertAlmostEqual(circle_area(5), math.pi * 25, places=7)

    def test_perimeter_positive(self):
        self.assertAlmostEqual(circle_perimeter(5), 2 * math.pi * 5, places=7)


class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(triangle_area(6, 4), 12)

    def test_perimeter_positive(self):
        self.assertEqual(triangle_perimeter(3, 4, 5), 12)

    def test_area_zero(self):
        self.assertEqual(triangle_area(0, 0), 0)


class SquareTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(square_area(4), 16)

    def test_perimeter(self):
        self.assertEqual(square_perimeter(4), 16)

    def test_area_zero(self):
        self.assertEqual(square_area(0), 0)


class RectangleTestCase(unittest.TestCase):
    def test_area_zero_mul(self):
        self.assertEqual(rectangle_area(10, 0), 0)

    def test_area_square_mul(self):
        self.assertEqual(rectangle_area(10, 10), 100)

    def test_perimeter(self):
        self.assertEqual(rectangle_perimeter(10, 10), 40)


if __name__ == "__main__":
    unittest.main()