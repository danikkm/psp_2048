# Game.py

from getch import getch

from GameLogic import GameLogic
from Movement import Movement
from SystemHelper import SystemHelper


class Game(GameLogic):

    def __init__(self, max_score, size):
        super().__init__(max_score, size)
        self.system_helper = SystemHelper()

    def swipe(self, pressed_key):
        pressed_key = self.system_helper.pressed_key(pressed_key)
        Movement.swipe(self, pressed_key)

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

    # TODO: When using arrow keys, reads multiple keystrokes at once
    @staticmethod
    def get_pressed_key():
        return ord(getch())
