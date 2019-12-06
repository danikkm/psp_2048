# Board.py

import termcolor

from Element import Element


class Board:
    __size = None
    __board = None
    __board_length = None
    __board_colors = None

    def __init__(self, size):
        self.element = Element()
        self.set_size(size)
        self.__board = self._create_board(size)
        self.__board_length = self.set_board_length()
        self.__board_colors = self.set_board_colors()
        self.randomly_generated_number_x = 0
        self.randomly_generated_number_y = 0

    def set_size(self, size):
        self.__size = size

    def _create_board(self, size):
        assert size > 1, "Wrong number, must be: > 1"
        assert type(size) == int, "Argument must be an int type"
        return [[self.element.get_empty_element() for _ in range(size)] for _ in range(size)]

    def get_board(self):
        return self.__board

    def set_board_length(self):
        return len(self.__board)

    def get_board_length(self):
        return self.__board_length

    @staticmethod
    def set_board_colors():
        return {
            '*': None,
            '2': 'red',
            '4': 'yellow',
            '8': 'green',
            '16': 'magenta',
            '32': 'cyan',
            '64': 'blue',
            '128': 'magenta',
            '256': 'white',
            '512': 'green',
            '1024': 'blue',
            '2048': 'red'
        }

    def get_board_colors(self):
        return self.__board_colors

    def draw_game_board(self):
        vertical_border = ""
        for i in range(self.get_board_length() + 2):
            vertical_border += "-\t"
        print(vertical_border)
        for y in range(self.get_board_length()):
            row = ""
            for x in self.get_board()[y]:
                if termcolor is not None:
                    row += termcolor.colored(x, self.get_board_colors()[x])
                else:
                    row += x
                row += "\t"

            print("|\t" + row + "|")
            if y is not self.get_board_length() - 1:
                print("")
        print(vertical_border)

    def board_is_full(self):
        for row in self.get_board():
            for element in row:
                if element == self.element.get_empty_element():
                    return False
        return True

    def place_random_element(self):
        if self.board_is_full():
            return False

        found_where_to_place = False

        while not found_where_to_place:
            self.randomly_generated_number_x = self.element.get_random_number(self.get_board_length())
            self.randomly_generated_number_y = self.element.get_random_number(self.get_board_length())

            found_where_to_place = self.get_object(self.randomly_generated_number_x,
                                                   self.randomly_generated_number_y) == '*'

        self.set_object(self.element.get_generated_number_in_range(), self.randomly_generated_number_x,
                        self.randomly_generated_number_y)

        return True

    def get_object(self, x_coordinate, y_coordinate):
        assert type(x_coordinate) == type(y_coordinate), "Values must be an int type"

        if self.given_coordinates_are_not_valid(x_coordinate, y_coordinate):
            return None

        return self.get_board()[y_coordinate][x_coordinate]

    def set_object(self, object_to_place, x_coordinate, y_coordinate):
        assert type(x_coordinate) == type(y_coordinate) == int, "Values must be an int types"

        if self.given_coordinates_are_not_valid(x_coordinate, y_coordinate):
            return False

        self.get_board()[y_coordinate][x_coordinate] = object_to_place

        return True

    def given_coordinates_are_not_valid(self, x_coordinate, y_coordinate):
        if x_coordinate >= self.get_board_length() or y_coordinate >= self.get_board_length() \
                or x_coordinate < 0 or y_coordinate < 0:
            return True
