# MovementSwipeDown.py

from GameLogic import GameLogic


class MovementSwipeDown(GameLogic):

    def __init__(self, max_score, size):
        super().__init__(max_score, size)

    def swipe(self, swipe_direction):
        swiped_down = False
        for y in range(self.board.get_board_length()):
            y = self.board.get_board_length() - 1 - y
            for x in range(self.board.get_board_length()):
                element_at_xy = self.board.get_element(x, y)
                element_below = self.board.get_element(x, y + 1)

                if element_at_xy == self.board.element.get_empty_element():
                    continue
                elif element_below is None:
                    continue

                swiped_down = self.move_element(x, y, swipe_direction) or swiped_down

        if swiped_down:
            self.swipe_current_element()
        else:
            self.do_nothing()
