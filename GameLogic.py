# GameLogic.py

import time
from abc import ABCMeta, abstractmethod

from Board import Board
from Score import Score
from SystemHelper import SystemHelper


class GameLogic(metaclass=ABCMeta):

    def __init__(self, max_score, size):
        self.score = Score(max_score)
        self.board = Board(size)

    def swipe_current_element(self):
        SystemHelper.flush_screen()
        self.board.draw_game_board()
        time.sleep(.3)
        self.board.place_random_element()
        SystemHelper.flush_screen()
        self.board.draw_game_board()

    def do_nothing(self):
        SystemHelper.flush_screen()
        self.board.draw_game_board()
        time.sleep(.3)

    @abstractmethod
    def swipe(self, pressed_key):
        """Swipe interface"""

    def move_element(self, x_coordinate, y_coordinate, direction_to_swipe):
        element_at_xy = self.board.get_element(x_coordinate, y_coordinate)

        assert element_at_xy != self.board.element.get_empty_element(), "Error in logic"

        valid_swipe_direction = ("UP" == direction_to_swipe or
                                 "DOWN" == direction_to_swipe or
                                 "LEFT" == direction_to_swipe or
                                 "RIGHT" == direction_to_swipe)

        assert valid_swipe_direction, "Invalid swipe direction"

        if direction_to_swipe == "UP":
            adjacent_element = (self.board.get_element(x_coordinate, y_coordinate - 1),
                                x_coordinate, y_coordinate - 1)

        elif direction_to_swipe == "DOWN":
            adjacent_element = (self.board.get_element(x_coordinate, y_coordinate + 1),
                                x_coordinate, y_coordinate + 1)
        elif direction_to_swipe == "LEFT":
            adjacent_element = (self.board.get_element(x_coordinate - 1, y_coordinate),
                                x_coordinate - 1, y_coordinate)
        elif direction_to_swipe == "RIGHT":
            adjacent_element = (self.board.get_element(x_coordinate + 1, y_coordinate),
                                x_coordinate + 1, y_coordinate)

        if adjacent_element[0] is None:  # edge of the board
            return False
        elif element_at_xy != adjacent_element[0] and adjacent_element[0] != \
                self.board.element.get_empty_element():  # cant combine 2 numbers
            return False

        elif adjacent_element[0] == self.board.element.get_empty_element():
            self.board.set_element(self.board.element.get_empty_element(), x_coordinate, y_coordinate)
            self.board.set_element(element_at_xy, adjacent_element[1], adjacent_element[2])
            self.move_element(adjacent_element[1], adjacent_element[2], direction_to_swipe)
            return True
        elif element_at_xy == adjacent_element[0]:
            self.board.set_element(self.board.element.get_empty_element(), x_coordinate, y_coordinate)
            self.board.set_element(str(int(adjacent_element[0]) * 2), adjacent_element[1], adjacent_element[2])
            self.move_element(adjacent_element[1], adjacent_element[2], direction_to_swipe)
            self.score.sum_session_score(int(adjacent_element[0]) * 2)
            return True
        else:
            assert False, "No way"

    def is_it_possible_to_swipe(self, x_coordinate, y_coordinate):
        element_at_xy = self.board.get_element(x_coordinate, y_coordinate)

        if element_at_xy is None:
            return False
        elif element_at_xy == self.board.element.get_empty_element():
            return True

        return (
                element_at_xy == self.board.get_element(x_coordinate, y_coordinate - 1) or
                element_at_xy == self.board.get_element(x_coordinate, y_coordinate + 1) or
                element_at_xy == self.board.get_element(x_coordinate - 1, y_coordinate) or
                element_at_xy == self.board.get_element(x_coordinate + 1, y_coordinate)
        )
