# Score.py


class Score:
    __score = None
    __max_score = None
    __current_digit = None

    def __init__(self, score):
        self.set_score(score)
        self.set_max_score(score)
        self.set_current_digit(score)

    @classmethod
    def set_score(cls, score):
        cls.__score = score

    @classmethod
    def get_score(cls):
        return cls.__score

    @classmethod
    def sum_score(cls, score):
        cls.__score += score

    @classmethod
    def set_max_score(cls, max_score):
        cls.__max_score = max_score

    @classmethod
    def get_max_score(cls):
        return cls.__max_score

    @classmethod
    def set_current_digit(cls, current_digit):
        cls.__current_digit = current_digit

    @classmethod
    def get_current_digit(cls):
        return cls.__current_digit