# TestGame.py

import unittest

from Game import Game


class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')


    def setUp(self):
        print('setUp')
        self.game_1 = Game(1024, 0, 4)
        self.game_2 = Game(16, 0, 3)


    def tearDown(self):
        print('tearDown\n')

    def test_create_board (self):
        print('test_create_board')
        self.assertEqual(self.game_1.board.get_board_length(), 4)
        self.assertEqual(self.game_2.board.get_board_length(), 3)

    def test_game_over(self):
        print('test_game_over')
        self.assertEqual(self.game_1.score.get_max_score(), 1024)
        self.assertEqual(self.game_2.score.get_max_score(), 16)

        self.game_1.score.set_max_score(2048)
        self.game_2.score.set_max_score(256)

        self.assertEqual(self.game_1.score.get_max_score(), 2048)
        self.assertEqual(self.game_2.score.get_max_score(), 256)

    def test_set_object(self):
        print('test_set_object')
        self.assertEqual(self.game_1.board.get_object(1,1), '*')
        self.assertEqual(self.game_1.board.get_object(-1, -1), None)




if __name__ == '__main__':
    unittest.main()






