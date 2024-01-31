from unittest import TestCase
from unittest.mock import patch

from simple_game import make_board


class TestMakeBoard(TestCase):
    @patch('random.choice', side_effect=['Empty room', 'Empty room', 'Empty room', 'Empty room'])
    def test_smallest_board_all_empty(self, _):
        expected = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        actual = make_board(2, 2)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['Empty room', 'Garden', 'Garden', 'Living room',
                                         'Empty room', 'Garden', 'Garden', 'Living room', 'Garden'])
    def test_square_board_different_room_type(self, _):
        expected = {(0, 0): 'Empty room', (0, 1): 'Garden', (0, 2): 'Garden', (1, 0): 'Living room',
                    (1, 1): 'Empty room', (1, 2): 'Garden', (2, 0): 'Garden', (2, 1): 'Living room',
                    (2, 2): 'Garden'}
        actual = make_board(3, 3)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['Empty room', 'Empty room', 'Empty room', 'Empty room',
                                         'Empty room', 'Empty room'])
    def test_rectangle_board_more_rows_all_empty(self, _):
        expected = {(0, 0): 'Empty room', (0, 1): 'Empty room',  (1, 0): 'Empty room',
                    (1, 1): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room'}
        actual = make_board(3, 2)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=['Living room', 'Living room', 'Empty room', 'Empty room',
                                         'Empty room', 'Garden'])
    def test_rectangle_board_more_columns_different_room_type(self, _):
        expected = {(0, 0): 'Living room', (0, 1): 'Living room', (0, 2): 'Empty room', (1, 0): 'Empty room',
                    (1, 1): 'Empty room', (1, 2): 'Garden'}
        actual = make_board(2, 3)
        self.assertEqual(expected, actual)
