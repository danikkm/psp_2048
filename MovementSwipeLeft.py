import time

from GameLogic import GameLogic
from SystemHelper import SystemHelper


class MovementSwipeLeft(GameLogic):

    def __init__(self, max_score, session_score, size):
        super().__init__(max_score, session_score, size)

    def swipe(self):
        swiped_left = False
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                object_at_xy = self.board.get_object(x, y)
                element_on_the_left = self.board.get_object(x - 1, y)

                if object_at_xy == self.board.element.get_empty_element():
                    continue

                elif element_on_the_left is None:
                    continue

                swiped_left = self.move_element(x, y, "LEFT") or swiped_left

        if swiped_left:
            self.swipe_current_element()
        else:
            SystemHelper.flush_screen()
            self.board.draw_game_board()
            time.sleep(.3)
