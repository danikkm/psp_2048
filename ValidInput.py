# ValidInput.py


class ValidInput:

    @staticmethod
    def is_power_of_two(number):
        return (number != 0) and (number & (number - 1) == 0)
