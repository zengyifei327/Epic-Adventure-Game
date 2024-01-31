from unittest import TestCase
from simple_game import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_top(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = '1'
        move_character(character, direction)
        expected = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        self.assertEqual(expected, character)

    def test_move_character_right(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = '2'
        move_character(character, direction)
        expected = {'X-coordinate': 2, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(expected, character)

    def test_move_character_down(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = '3'
        move_character(character, direction)
        expected = {'X-coordinate': 1, 'Y-coordinate': 2, 'Current HP': 5}
        self.assertEqual(expected, character)

    def test_move_character_left(self):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        direction = '4'
        move_character(character, direction)
        expected = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        self.assertEqual(expected, character)
