# Element.py

import random


class Element:
    __empty_element = None

    def __init__(self):
        self.__empty_element = "*"
        self.digit_to_place = None

    def get_empty_element(self):
        return self.__empty_element

    @staticmethod
    def get_random_number(number_range):
        return random.randrange(number_range)

    def get_generated_number_in_range(self):

        randomly_generated_number = self.get_random_number(100)

        if randomly_generated_number < 60:
            self.digit_to_place = "2"

        elif 90 > randomly_generated_number >= 60:
            self.digit_to_place = "4"

        else:
            self.digit_to_place = "8"

        return self.digit_to_place
