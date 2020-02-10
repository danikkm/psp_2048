# test_board.py

import unittest

from board import Board


class TestBoard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.board = Board(4)

    def tearDown(self):
        print('tearDown\n')

    def test_create_board(self):
        print('test_create_board')

        # Action

        expected_result = self.board.get_board()

        # Assert

        self.assertEqual(self.board.get_board(), expected_result)

    def test_board_is_full(self):
        print('test_board_is_full')

        # Action

        expected_result = self.board.board_is_full()

        # Assert

        self.assertFalse(expected_result)

    def test_set_object(self):
        print('test_set_object')

        # Action

        expected_result = self.board.set_element("2", -1, -1)

        # Assert

        self.assertFalse(expected_result)


if __name__ == '__main__':
    unittest.main()
