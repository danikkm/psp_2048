import time

from GameLogic import GameLogic
from SystemHelper import SystemHelper


class MovementSwipeRight(GameLogic):
    def __init__(self, max_score, size):
        super().__init__(max_score, size)

    def swipe(self):
        swiped_right = False
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                x = self.board.get_board_length() - 1 - x

                element_at_xy = self.board.get_element(x, y)
                element_on_the_right = self.board.get_element(x + 1, y)

                if element_at_xy == self.board.element.get_empty_element():
                    continue
                elif element_on_the_right is None:
                    continue

                swiped_right = self.move_element(x, y, "RIGHT") or swiped_right

        if swiped_right:
            self.swipe_current_element()
        else:
            SystemHelper.flush_screen()
            self.board.draw_game_board()
            time.sleep(.3)
