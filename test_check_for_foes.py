from unittest import TestCase
from unittest.mock import patch
from simple_game import check_for_foes


class TestCheckForFoes(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_random_number_is_1(self, _):
        actual = check_for_foes()
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[2])
    def test_random_number_is_2(self, _):
        actual = check_for_foes()
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[3])
    def test_random_number_is_3(self, _):
        actual = check_for_foes()
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', side_effect=[4])
    def test_random_number_is_4(self, _):
        actual = check_for_foes()
        expected = False
        self.assertEqual(expected, actual)