# test_board.py

import unittest

from score import Score


class TestBoard(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.score = Score(2048)

    def tearDown(self):
        print('tearDown\n')

    def test_get_max_score(self):
        print('test_get_max_score')

        # Action

        expected_result = 2048

        # Assert

        self.assertEqual(self.score.get_max_score(), expected_result)


if __name__ == '__main__':
    unittest.main()
