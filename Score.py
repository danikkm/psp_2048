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
    def sum_session_score(cls, session_score):
        cls.__session_score += session_score

    @classmethod
    def set_session_score(cls, session_score):
        cls.__session_score = session_score

    @classmethod
    def sum_score(cls, score):
        cls.__score += score

    @classmethod
    def set_max_score(cls, max_score):
        cls.__max_score = max_score

    @classmethod
    def get_max_score(cls):
        return cls.__max_score
