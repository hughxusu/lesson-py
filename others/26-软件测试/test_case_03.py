import unittest
from distances import distance

class DistanceCalculationTest(unittest.TestCase):
    def setUp(self):
        self.point1 = [1, 2, 3]
        self.point2 = [4, 5, 6]
        self.point5 = [1, 2]
        self.point6 = [1, 2, 3, 4]

    def test_01(self):
        self.assertAlmostEqual(distance(self.point1, self.point2), 5.196152, places=6)

    def test_02(self):
        self.assertEqual(distance(self.point1, self.point1), 0)

    def test_03(self):
        with self.assertRaises(ValueError):
            distance(self.point5, self.point6)

if __name__ == '__main__':
    unittest.main()