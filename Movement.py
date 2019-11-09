# Movement.py

import time
from SystemHelper import SystemHelper
from GameBoard import GameBoard
from getch import getch


class Movement(GameBoard):

    @classmethod
    def swipe_current_element(cls, game_board):
        SystemHelper.flush_screen()
        game_board.draw_game_board()
        time.sleep(.3)
        game_board.place_random_element()
        SystemHelper.flush_screen()
        game_board.draw_game_board()

    def movement_swipe_up(self):
        swiped = False
        for y in range(self.matrix_length):
            for x in range(self.matrix_length):
                object_at_xy = self.get_object(x, y)
                element_above = self.get_object(x, y - 1)

                if object_at_xy == "*":
                    continue

                elif element_above is None:
                    continue

                swiped = self.move_element(x, y, "UP") or swiped

        if swiped:
            Movement.swipe_current_element(self)
        else:
            SystemHelper.flush_screen()
            self.draw_game_board()
            time.sleep(.3)

    def movement_swipe_down(self):
        swiped = False

        for y in range(self.matrix_length):
            y = self.matrix_length - 1 - y

            for x in range(self.matrix_length):
                object_at_xy = self.get_object(x, y)
                element_below = self.get_object(x, y + 1)

                if object_at_xy == "*":
                    continue
                elif element_below is None:
                    continue

                swiped = self.move_element(x, y, "DOWN") or swiped
        if swiped:
            Movement.swipe_current_element(self)
        else:
            SystemHelper.flush_screen()
            self.draw_game_board()
            time.sleep(.3)

    def movement_swipe_left(self):
        swiped = False

        for y in range(self.matrix_length):
            for x in range(self.matrix_length):
                object_at_xy = self.get_object(x, y)
                element_on_the_left = self.get_object(x - 1, y)

                if object_at_xy == "*":
                    continue
                elif element_on_the_left is None:
                    continue

                swiped = self.move_element(x, y, "LEFT") or swiped

        if swiped:
            Movement.swipe_current_element(self)
        else:
            SystemHelper.flush_screen()
            self.draw_game_board()
            time.sleep(.3)

    def movement_swipe_right(self):
        swiped = False

        for y in range(self.matrix_length):
            for x in range(self.matrix_length):
                x = self.matrix_length - 1 - x

                object_at_xy = self.get_object(x, y)
                element_on_the_right = self.get_object(x + 1, y)

                if object_at_xy == "*":
                    continue
                elif element_on_the_right is None:
                    continue

                swiped = self.move_element(x, y, "RIGHT") or swiped

        if swiped:
            Movement.swipe_current_element(self)
        else:
            SystemHelper.flush_screen()
            self.draw_game_board()
            time.sleep(.3)

    def game_over(self):
        for y in range(self.matrix_length):
            for x in range(self.matrix_length):
                if self.is_it_possible_to_swipe(x, y):
                    return False
        return True

    # todo: fix getch catches length 0
    @staticmethod
    def get_pressed_key():
        return ord(getch())
