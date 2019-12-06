# GameLogic.py
import time

from Board import Board
from Score import Score
from SystemHelper import SystemHelper


class GameLogic:

    def __init__(self, max_score, session_score, size):
        self.score = Score(max_score, session_score)

        self.board = Board(size)

    def swipe_current_element(self):
        SystemHelper.flush_screen()
        self.board.draw_game_board()
        time.sleep(.3)
        self.board.place_random_element()
        SystemHelper.flush_screen()
        self.board.draw_game_board()

    def move_element(self, x_coordinate, y_coordinate, direction_to_swipe):
        object_at_xy = self.board.get_object(x_coordinate, y_coordinate)

        assert object_at_xy != self.board.element.get_empty_element(), "Error in logic"

        valid_swipe_direction = ("UP" == direction_to_swipe or
                                 "DOWN" == direction_to_swipe or
                                 "LEFT" == direction_to_swipe or
                                 "RIGHT" == direction_to_swipe)

        assert valid_swipe_direction, "Invalid swipe direction"

        if direction_to_swipe == "UP":
            adjacent_object = (self.board.get_object(x_coordinate, y_coordinate - 1),
                               x_coordinate, y_coordinate - 1)

        elif direction_to_swipe == "DOWN":
            adjacent_object = (self.board.get_object(x_coordinate, y_coordinate + 1),
                               x_coordinate, y_coordinate + 1)
        elif direction_to_swipe == "LEFT":
            adjacent_object = (self.board.get_object(x_coordinate - 1, y_coordinate),
                               x_coordinate - 1, y_coordinate)
        elif direction_to_swipe == "RIGHT":
            adjacent_object = (self.board.get_object(x_coordinate + 1, y_coordinate),
                               x_coordinate + 1, y_coordinate)

        if adjacent_object[0] is None:  # edge of the board
            return False
        elif object_at_xy != adjacent_object[0] and adjacent_object[0] != "*":  # cant combine 2 numbers
            return False

        elif adjacent_object[0] == self.board.element.get_empty_element():
            self.board.set_object(self.board.element.get_empty_element(), x_coordinate, y_coordinate)
            self.board.set_object(object_at_xy, adjacent_object[1], adjacent_object[2])
            self.move_element(adjacent_object[1], adjacent_object[2], direction_to_swipe)
            return True
        elif object_at_xy == adjacent_object[0]:
            self.board.set_object(self.board.element.get_empty_element(), x_coordinate, y_coordinate)
            self.board.set_object(str(int(adjacent_object[0]) * 2), adjacent_object[1], adjacent_object[2])
            self.move_element(adjacent_object[1], adjacent_object[2], direction_to_swipe)
            self.score.sum_session_score(int(adjacent_object[0]) * 2)
            return True
        else:
            assert False, "No way"

    def is_it_possible_to_swipe(self, x_coordinate, y_coordinate):
        object_at_xy = self.board.get_object(x_coordinate, y_coordinate)

        if object_at_xy is None:
            return False
        elif object_at_xy == self.board.element.get_empty_element():
            return True

        return (
                object_at_xy == self.board.get_object(x_coordinate, y_coordinate - 1) or
                object_at_xy == self.board.get_object(x_coordinate, y_coordinate + 1) or
                object_at_xy == self.board.get_object(x_coordinate - 1, y_coordinate) or
                object_at_xy == self.board.get_object(x_coordinate + 1, y_coordinate)
        )
