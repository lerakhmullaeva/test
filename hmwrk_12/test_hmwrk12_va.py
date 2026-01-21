import unittest
from hmwrk_12.homeworks import add_numbers, dishes, photobook, garden, temperature

class TestHomework12(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(10, 4), 14)

    def test_dishes(self):
        self.assertEqual(dishes(274, 218, 35, 350, 21), 2085)

    def test_photobook(self):
        self.assertEqual(photobook(232, 8), 29)

    def test_garden(self):
        self.assertEqual(garden(24, 1, 2), 33)

    def test_temperature(self):
        self.assertEqual(temperature(5), -1)

if __name__ == "__main__":
    unittest.main()