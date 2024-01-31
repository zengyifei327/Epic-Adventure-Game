from unittest import TestCase
from simple_game import is_alive


class TestIsAlive(TestCase):
    def test_HP_is_5(self):
        expected = True
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_HP_is_4(self):
        expected = True
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 4}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_HP_is_3(self):
        expected = True
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 3}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_HP_is_2(self):
        expected = True
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 2}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_HP_is_1(self):
        expected = True
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 1}
        actual = is_alive(character)
        self.assertEqual(expected, actual)

    def test_HP_is_0(self):
        expected = False
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 0}
        actual = is_alive(character)
        self.assertEqual(expected, actual)
