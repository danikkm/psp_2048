# MovementSwipeUp.py


from GameLogic import GameLogic


class MovementSwipeUp(GameLogic):

    def swipe(self, swipe_direction):
        swiped_up = False
        for y in range(self.board.get_board_length()):
            for x in range(self.board.get_board_length()):
                element_at_xy = self.board.get_element(x, y)
                element_above = self.board.get_element(x, y - 1)

                if element_at_xy == self.board.element.get_empty_element():
                    continue

                elif element_above is None:
                    continue

                swiped_up = self.move_element(x, y, swipe_direction) or swiped_up

        if swiped_up:
            self.swipe_current_element()
        else:
            self.do_nothing()
