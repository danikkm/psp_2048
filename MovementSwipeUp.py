import time

from GameLogic import GameLogic
from SystemHelper import SystemHelper


class MovementSwipeUp(GameLogic):

    def __init__(self, max_score, session_score, size):
        super().__init__(max_score, session_score, size)

    def swipe(self):
        swiped_up = False
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                object_at_xy = self.board.get_object(x, y)
                element_above = self.board.get_object(x, y - 1)

                if object_at_xy == self.board.element.get_empty_element():
                    continue

                elif element_above is None:
                    continue

                swiped_up = self.move_element(x, y, "UP") or swiped_up

        if swiped_up:
            self.swipe_current_element()
        else:
            SystemHelper.flush_screen()
            self.board.draw_game_board()
            time.sleep(.3)
