from unittest import TestCase
from simple_game import check_if_goal_attained


class TestCheckGoal(TestCase):
    def test_goal_attained(self):
        expected = True
        board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_goal_not_attained_one_move_away(self):
        expected = False
        board = {(0, 0): 'Empty room', (0, 1): 'Empty room',  (1, 0): 'Empty room',
                 (1, 1): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room'}
        character = {'X-coordinate': 2, 'Y-coordinate': 0, 'Current HP': 5}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)

    def test_goal_not_attained_many_moves_away(self):
        expected = False
        board = {(0, 0): 'Empty room', (0, 1): 'Empty room',  (1, 0): 'Empty room',
                 (1, 1): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        actual = check_if_goal_attained(board, character)
        self.assertEqual(expected, actual)