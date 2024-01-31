from unittest import TestCase
from simple_game import validate_move


class TestValidMove(TestCase):
    def test_can_move_top(self):
        expected = True
        my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        my_character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        my_direction = '1'
        actual = validate_move(my_board, my_character, my_direction)
        self.assertEqual(expected, actual)

    def test_can_not_move_top(self):
        expected = False
        my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        my_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        my_direction = '1'
        actual = validate_move(my_board, my_character, my_direction)
        self.assertEqual(expected, actual)

    def test_can_move_right(self):
        expected = True
        my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        my_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        my_direction = '2'
        actual = validate_move(my_board, my_character, my_direction)
        self.assertEqual(expected, actual)

    def test_can_not_move_right(self):
        expected = False
        my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        my_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        my_direction = '2'
        actual = validate_move(my_board, my_character, my_direction)
        self.assertEqual(expected, actual)

    def test_can_move_down(self):
        expected = True
        my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        my_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        my_direction = '3'
        actual = validate_move(my_board, my_character, my_direction)
        self.assertEqual(expected, actual)

    def test_can_not_move_down(self):
        expected = False
        my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        my_character = {'X-coordinate': 0, 'Y-coordinate': 1, 'Current HP': 5}
        my_direction = '3'
        actual = validate_move(my_board, my_character, my_direction)
        self.assertEqual(expected, actual)

    def test_can_move_left(self):
        expected = True
        my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room',
                    (1, 1): 'Empty room', (1, 2): 'Empty room'}
        my_character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        my_direction = '4'
        actual = validate_move(my_board, my_character, my_direction)
        self.assertEqual(expected, actual)

    def test_can_not_move_left(self):
        expected = False
        my_board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room',
                    (1, 1): 'Empty room', (1, 2): 'Empty room'}
        my_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        my_direction = '4'
        actual = validate_move(my_board, my_character, my_direction)
        self.assertEqual(expected, actual)
