# Score.py


class Score:
    __score = None

    def __init__(self, score):
        self.set_score(score)

    @classmethod
    def set_score(cls, score):
        cls.__score = score

    @classmethod
    def get_score(cls):
        return cls.__score

    @classmethod
    def add_score(cls, score):
        cls.__score += score
