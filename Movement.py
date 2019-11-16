# Movement.py

import time

from getch import getch

from GameBoard import GameBoard
from SystemHelper import SystemHelper


class Movement(GameBoard):
    swiped = None

    def __init__(self, max_score, session_score, size):
        super().__init__(max_score, session_score, size)

    def swipe_current_element(self):
        SystemHelper.flush_screen()
        self.draw_game_board()
        time.sleep(.3)
        self.place_random_element()
        SystemHelper.flush_screen()
        self.draw_game_board()

    def movement_swipe_up(self):
        for y in range(self.matrix_length):
            for x in range(self.matrix_length):
                object_at_xy = self.get_object(x, y)
                element_above = self.get_object(x, y - 1)

                if object_at_xy == "*":
                    continue

                elif element_above is None:
                    continue

                self.swiped = self.move_element(x, y, "UP") or self.swiped

        if self.swiped:
            Movement.swipe_current_element(self)
        else:
            SystemHelper.flush_screen()
            self.draw_game_board()
            time.sleep(.3)

    def movement_swipe_down(self):

        for y in range(self.matrix_length):
            y = self.matrix_length - 1 - y

            for x in range(self.matrix_length):
                object_at_xy = self.get_object(x, y)
                element_below = self.get_object(x, y + 1)

                if object_at_xy == "*":
                    continue
                elif element_below is None:
                    continue

                self.swiped = self.move_element(x, y, "DOWN") or self.swiped
        if self.swiped:
            Movement.swipe_current_element(self)
        else:
            SystemHelper.flush_screen()
            self.draw_game_board()
            time.sleep(.3)

    def movement_swipe_left(self):

        for y in range(self.matrix_length):
            for x in range(self.matrix_length):
                object_at_xy = self.get_object(x, y)
                element_on_the_left = self.get_object(x - 1, y)

                if object_at_xy == "*":
                    continue
                elif element_on_the_left is None:
                    continue

                self.swiped = self.move_element(x, y, "LEFT") or self.swiped

        if self.swiped:
            Movement.swipe_current_element(self)
        else:
            SystemHelper.flush_screen()
            self.draw_game_board()
            time.sleep(.3)

    def movement_swipe_right(self):

        for y in range(self.matrix_length):
            for x in range(self.matrix_length):
                x = self.matrix_length - 1 - x

                object_at_xy = self.get_object(x, y)
                element_on_the_right = self.get_object(x + 1, y)

                if object_at_xy == "*":
                    continue
                elif element_on_the_right is None:
                    continue

                self.swiped = self.move_element(x, y, "RIGHT") or self.swiped

        if self.swiped:
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

    def reached_max_score(self):
        for y in range(self.matrix_length):
            for x in range(len(self.get_board()[0])):
                if self.get_board()[y][x] == str(self.score.get_max_score()):
                    return True

    # todo: fix getch catches length 0
    @staticmethod
    def get_pressed_key():
        return ord(getch())
