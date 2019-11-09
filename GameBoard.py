# GameBoard.py

import random
import termcolor
from Score import Score


class GameBoard:

    def __init__(self, size):
        self.sessionScore = Score(0)
        self.board_matrix = self._create_game_board(size)
        self.board_colors = self._set_board_colors()
        self.matrix_length = self._get_board_len()
        self.randomly_generated_number_x = 0
        self.randomly_generated_number_y = 0

    def get_board(self):
        return self.board_matrix

    @staticmethod
    def _create_game_board(size):
        assert size > 1, "Wrong number, must be: > 1"
        assert type(size) == int, "Argument must be an int type"
        return [["*" for x in range(size)] for x in range(size)]

    @staticmethod
    def _set_board_colors():
        return {
            '*': None,
            '2': 'red',
            '4': 'yellow',
            '8': 'green',
            '16': 'magenta',
            '32': 'cyan',
            '64': 'blue',
            '128': 'grey',
            '256': 'white',
            '512': 'green',
            '1024': 'blue',
            '2048': 'red'
        }
    
    def _get_board_len(self):
        return len(self.board_matrix)

    def draw_game_board(self):
        vertical_border = ""
        for i in range(self.matrix_length + 2):
            vertical_border += "-\t"
        print(vertical_border)
        for y in range(self.matrix_length):
            row = ""
            for x in self.board_matrix[y]:

                if termcolor is not None:
                    row += termcolor.colored(x, self.board_colors[x])
                else:
                    row += x
                row += "\t"

            print("|\t" + row + "|")
            if y is not self.matrix_length - 1:
                print("")
        print(vertical_border)

    def place_random_element(self):
        if self.board_is_full():
            print("not supposed to be here")
            return False

        randomly_generated_number = self.get_random_number(100)

        if randomly_generated_number < 60:
            digit_to_place = "2"

        elif 90 > randomly_generated_number >= 60:
            digit_to_place = "4"

        else:
            digit_to_place = "8"
        found_place = False
        while not found_place:

            self.randomly_generated_number_x = self.get_random_number(self.matrix_length)
            self.randomly_generated_number_y = self.get_random_number(self.matrix_length)

            found_place = self.get_object(self.randomly_generated_number_x, self.randomly_generated_number_y) == '*'

        self.set_object(digit_to_place, self.randomly_generated_number_x, self.randomly_generated_number_y)

        return True

    @staticmethod
    def get_random_number(number_range):
        return random.randrange(number_range)

    def board_is_full(self):
        for row in self.get_board():
            for element in row:
                if element == "*":
                    return False
        return True

    def get_object(self, x_coordinate, y_coordinate):
        assert type(x_coordinate) == type(y_coordinate), "Values must be an int type"

        if x_coordinate >= self.matrix_length or y_coordinate >= len(
                self.board_matrix) or x_coordinate < 0 or y_coordinate < 0:
            return None

        return self.board_matrix[y_coordinate][x_coordinate]

    def set_object(self, object_to_place, x_coordinate, y_coordinate):
        assert type(x_coordinate) == type(y_coordinate) == int, "Values must be an int types"

        if x_coordinate >= self.matrix_length or y_coordinate >= len(
                self.board_matrix) or x_coordinate < 0 or y_coordinate < 0:
            return False

        self.board_matrix[y_coordinate][x_coordinate] = object_to_place
        return True

    def move_element(self, x_coordinate, y_coordinate, direction_to_swipe):
        object_at_xy = self.get_object(x_coordinate, y_coordinate)

        assert object_at_xy != "*", "Error in logic"

        valid_swipe_direction = ("UP" == direction_to_swipe or
                                 "DOWN" == direction_to_swipe or
                                 "LEFT" == direction_to_swipe or
                                 "RIGHT" == direction_to_swipe)

        assert valid_swipe_direction, "Invalid swipe direction"

        if direction_to_swipe == "UP":
            adjacent_object = (self.get_object(x_coordinate, y_coordinate - 1),
                               x_coordinate, y_coordinate - 1)
            # debug
            # print("Swiped", directionToSwipe, "supposed to swipe:", "up")

        elif direction_to_swipe == "DOWN":
            adjacent_object = (self.get_object(x_coordinate, y_coordinate + 1),
                               x_coordinate, y_coordinate + 1)
            # debug
            # print("Swiped", directionToSwipe, "supposed to swipe:", "down")

        elif direction_to_swipe == "LEFT":
            adjacent_object = (self.get_object(x_coordinate - 1, y_coordinate),
                               x_coordinate - 1, y_coordinate)
            # debug
            # print("Swiped", directionToSwipe, "supposed to swipe:", "left")

        elif direction_to_swipe == "RIGHT":
            adjacent_object = (self.get_object(x_coordinate + 1, y_coordinate),
                               x_coordinate + 1, y_coordinate)
            # debug
            # print("Swiped", directionToSwipe, "supposed to swipe:", "right")

        if adjacent_object[0] is None:  # edge of the board
            return False
        elif object_at_xy != adjacent_object[0] and adjacent_object[0] != "*":  # cant combine 2 numbers
            return False

        elif adjacent_object[0] == "*":
            self.set_object("*", x_coordinate, y_coordinate)
            self.set_object(object_at_xy, adjacent_object[1], adjacent_object[2])
            self.move_element(adjacent_object[1], adjacent_object[2], direction_to_swipe)
            return True
        elif object_at_xy == adjacent_object[0]:
            self.set_object("*", x_coordinate, y_coordinate)
            self.set_object(str(int(adjacent_object[0]) * 2), adjacent_object[1], adjacent_object[2])
            self.move_element(adjacent_object[1], adjacent_object[2], direction_to_swipe)

            Score.add_score(int(adjacent_object[0]) * 2)

            return True
        else:
            assert False, "No way"

        return False

    def is_it_possible_to_swipe(self, x_coordinate, y_coordinate):
        object_at_xy = self.get_object(x_coordinate, y_coordinate)

        if object_at_xy is None:
            return False
        elif object_at_xy == "*":
            return True

        return (
                object_at_xy == self.get_object(x_coordinate, y_coordinate - 1) or
                object_at_xy == self.get_object(x_coordinate, y_coordinate + 1) or
                object_at_xy == self.get_object(x_coordinate - 1, y_coordinate) or
                object_at_xy == self.get_object(x_coordinate + 1, y_coordinate)
        )
