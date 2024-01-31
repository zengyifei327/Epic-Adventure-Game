from unittest import TestCase
import unittest.mock
import io

from simple_game import describe_current_location


class TestPrintLocation(TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_location_empty_room_full_HP(self, mock_stdout):
        expected = ('Your current location is (0, 0), this room is Empty room, your current HP is 5. '
                    'You need to reach (1, 1) while remaining alive to win the game.\n')
        board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        describe_current_location(board, character)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_location_garden_not_full_HP(self, mock_stdout):
        expected = ('Your current location is (0, 0), this room is Garden, your current HP is 4. You need to reach (1, '
                    '1) while remaining alive to win the game.\n')
        board = {(0, 0): 'Garden', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 4}
        describe_current_location(board, character)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_user_move_location_living_room_full_HP(self, mock_stdout):
        expected = ('Your current location is (1, 0), this room is Living room, your current HP is 5. You need to '
                    'reach (1, 1) while remaining alive to win the game.\n')
        board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Living room', (1, 1): 'Empty room'}
        character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 5}
        describe_current_location(board, character)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_user_move_location_empty_room_not_full_HP(self, mock_stdout):
        expected = ('Your current location is (1, 0), this room is Empty room, your current HP is 3. '
                    'You need to reach (1, 1) while remaining alive to win the game.\n')
        board = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        character = {'X-coordinate': 1, 'Y-coordinate': 0, 'Current HP': 3}
        describe_current_location(board, character)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_starting_location_garden_full_HP_rectangle_board(self, mock_stdout):
        expected = ('Your current location is (0, 0), this room is Garden, your current HP is 5. You need to reach (1, '
                    '3) while remaining alive to win the game.\n')
        board = {(0, 0): 'Garden', (0, 1): 'Empty room',  (0, 2): 'Empty room',  (0, 3): 'Empty room',
                 (1, 0): 'Empty room', (1, 1): 'Empty room', (1, 2): 'Empty room', (1, 3): 'Empty room'}
        character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
        describe_current_location(board, character)
        self.assertEqual(mock_stdout.getvalue(), expected)