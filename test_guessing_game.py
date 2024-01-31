from unittest import TestCase
from unittest.mock import patch
import io

from simple_game import guessing_game


class TestGuessingGame(TestCase):
    @patch('builtins.input', side_effect=[1])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_1_guess_right(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'You guessed it right, well done!\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_1_guess_wrong(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Wrong number! The correct number is 1.You lost 1 HP. Your current HP is 4\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_2_guess_right(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'You guessed it right, well done!\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[1])
    @patch('random.randint', return_value=2)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_2_guess_wrong(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Wrong number! The correct number is 2.You lost 1 HP. Your current HP is 4\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[3])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_3_guess_right(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 4}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'You guessed it right, well done!\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_3_guess_wrong(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 4}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Wrong number! The correct number is 3.You lost 1 HP. Your current HP is 3\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[4])
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_4_guess_right(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'You guessed it right, well done!\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', return_value=4)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_4_guess_wrong(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Wrong number! The correct number is 4.You lost 1 HP. Your current HP is 4\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[5])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_5_guess_right(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 5}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'You guessed it right, well done!\n'
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('builtins.input', side_effect=[2])
    @patch('random.randint', return_value=5)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_random_number_5_guess_wrong(self, mock_output, _, __):
        character = {'X-coordinate': 1, 'Y-coordinate': 1, 'Current HP': 3}
        guessing_game(character)
        the_game_printed_this = mock_output.getvalue()
        expected_output = 'Wrong number! The correct number is 5.You lost 1 HP. Your current HP is 2\n'
        self.assertEqual(expected_output, the_game_printed_this)
