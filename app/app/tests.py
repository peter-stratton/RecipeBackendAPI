from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_whole_numbers(self):
        self.assertEqual(add(3, 8), 11)

    def test_subtract_whole_numbers(self):
        self.assertEqual(subtract(5, 3), 2)
