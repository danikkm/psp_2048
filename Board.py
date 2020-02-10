# Board.py

import termcolor

from BoardDecorator import BoardDecorator
from Element import Element
from gui_drawer import GUIDrawer


class Board:
    __size = None
    __board = None
    __board_length = None

    def __init__(self, size):
        self.element = Element()
        self.gui_drawer = GUIDrawer()
        self.gui_drawer.enable_gui()
        self.board_decorator = BoardDecorator()
        self.set_size(size)
        self.__board = self.create_board(size)
        self.__board_length = self.set_board_length()

        self.randomly_generated_number_x = 0
        self.randomly_generated_number_y = 0

    def set_size(self, size):
        self.__size = size

    def create_board(self, size):
        assert size > 1, "Wrong number, must be: > 1"
        assert type(size) == int, "Argument must be an int type"
        return [[self.element.get_empty_element() for _ in range(size)] for _ in range(size)]

    def get_board(self):
        return self.__board

    def set_board_length(self):
        return len(self.__board)

    def get_board_length(self):
        return self.__board_length

    def draw_game_board(self):
        vertical_border = ""
        for i in range(self.get_board_length() + 2):
            vertical_border += "-\t"
        print(vertical_border)
        for y in range(self.get_board_length()):
            row = ""
            for x in self.get_board()[y]:
                if termcolor is not None:
                    row += termcolor.colored(x, self.board_decorator.get_board_colors()[x])
                else:
                    row += x
                row += "\t"

            print("|\t" + row + "|")
            if y is not self.get_board_length() - 1:
                print("")
        print(vertical_border)

        if self.gui_drawer.is_gui_runnable():
            self.gui_drawer.get_gui().update_grid(self.get_board())
            self.gui_drawer.get_gui().update()

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

            found_where_to_place = self.get_element(self.randomly_generated_number_x,
                                                    self.randomly_generated_number_y) == self.element.get_empty_element()

        self.set_element(self.element.get_generated_number_in_range(), self.randomly_generated_number_x,
                         self.randomly_generated_number_y)

        return True

    def get_element(self, x_coordinate, y_coordinate):
        assert type(x_coordinate) == type(y_coordinate), "Values must be an int type"

        if self.given_coordinates_are_not_valid(x_coordinate, y_coordinate):
            return None

        return self.get_board()[y_coordinate][x_coordinate]

    def set_element(self, object_to_place, x_coordinate, y_coordinate):
        assert type(x_coordinate) == type(y_coordinate) == int, "Values must be an int types"

        if self.given_coordinates_are_not_valid(x_coordinate, y_coordinate):
            return False

        self.get_board()[y_coordinate][x_coordinate] = object_to_place

        return True

    def given_coordinates_are_not_valid(self, x_coordinate, y_coordinate):
        if x_coordinate >= self.get_board_length() or y_coordinate >= self.get_board_length() \
                or x_coordinate < 0 or y_coordinate < 0:
            return True
