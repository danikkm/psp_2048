# MovementSwipeLeft.py

from GameLogic import GameLogic


class MovementSwipeLeft(GameLogic):

    def __init__(self, max_score, size):
        super().__init__(max_score, size)

    def swipe(self, swipe_direction):
        swiped_left = False
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                element_at_xy = self.board.get_element(x, y)
                element_on_the_left = self.board.get_element(x - 1, y)

                if element_at_xy == self.board.element.get_empty_element():
                    continue

                elif element_on_the_left is None:
                    continue

                swiped_left = self.move_element(x, y, swipe_direction) or swiped_left

        if swiped_left:
            self.swipe_current_element()
        else:
            self.do_nothing()
