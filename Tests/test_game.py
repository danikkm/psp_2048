# test_board.py

import unittest

from game import Game


class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.game = Game(2048, 4)

    def tearDown(self):
        print('tearDown\n')

    def test_game_over(self):
        print('test_game_over')

        # Action

        expected_result = self.game.game_over()

        # Assert

        self.assertFalse(expected_result)

    def test_reached_max_score(self):
        print('test_reached_max_score')

        # Action

        expected_result = self.game.reached_max_score()

        # Assert

        self.assertFalse(expected_result)


if __name__ == '__main__':
    unittest.main()
