# Score.py


class Score:
    __max_score = None
    __session_score = None

    def __init__(self, max_score, session_score):
        self.set_session_score(session_score)
        self.set_max_score(max_score)

    @classmethod
    def sum_session_score(cls, session_score):
        cls.__session_score += session_score

    @classmethod
    def set_session_score(cls, session_score):
        cls.__session_score = session_score

    @classmethod
    def get_session_score(cls):
        return cls.__session_score

    @classmethod
    def set_max_score(cls, max_score):
        cls.__max_score = max_score

    @classmethod
    def get_max_score(cls):
        return cls.__max_score
