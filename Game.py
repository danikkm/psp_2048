# Game.py

from getch import getch

from GameLogic import GameLogic
from Movement import Movement


class Game(GameLogic):

    def __init__(self, max_score, session_score, size):
        super().__init__(max_score, session_score, size)

    def movement_swipe_up(self):
        Movement.swipe_up(self)

    def movement_swipe_down(self):
        Movement.swipe_down(self)

    def movement_swipe_left(self):
        Movement.swipe_left(self)

    def movement_swipe_right(self):
        Movement.swipe_right(self)

    def game_over(self):
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                if self.is_it_possible_to_swipe(x, y):
                    return False
        return True

    def reached_max_score(self):
        for y in range(self.board.get_board_length()):
            for x in range(len(self.board.get_board()[0])):
                if self.board.get_board()[y][x] == str(self.score.get_max_score()):
                    return True

    # todo: fix getch catches length 0
    @staticmethod
    def get_pressed_key():
        return ord(getch())
