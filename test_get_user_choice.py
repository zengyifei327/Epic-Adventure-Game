from unittest import TestCase
from unittest.mock import patch

from simple_game import get_user_choice


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_user_choose_1(self, _):
        expected = '1'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_user_choose_2(self, _):
        expected = '2'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_user_choose_3(self, _):
        expected = '3'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['4'])
    def test_user_choose_4(self, _):
        expected = '4'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['x', '1'])
    def test_one_invalid_input(self, _):
        expected = '1'
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['?', 'idk', 'what', '3'])
    def test_many_invalid_inputs(self, _):
        expected = '3'
        actual = get_user_choice()
        self.assertEqual(expected, actual)