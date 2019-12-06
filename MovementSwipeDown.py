import time

from GameLogic import GameLogic
from SystemHelper import SystemHelper


class MovementSwipeDown(GameLogic):

    def __init__(self, max_score, session_score, size):
        super().__init__(max_score, session_score, size)

    def swipe(self):
        swiped_down = False
        for y in range(self.board.get_board_length()):
            y = self.board.get_board_length() - 1 - y

            for x in range(self.board.get_board_length()):
                object_at_xy = self.board.get_object(x, y)
                element_below = self.board.get_object(x, y + 1)

                if object_at_xy == self.board.element.get_empty_element():
                    continue
                elif element_below is None:
                    continue

                swiped_down = self.move_element(x, y, "DOWN") or swiped_down
        if swiped_down:
            self.swipe_current_element()
        else:
            SystemHelper.flush_screen()
            self.board.draw_game_board()
            time.sleep(.3)