from unittest import TestCase
from simple_game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        expected = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        actual = make_character()
        self.assertEqual(expected, actual)
