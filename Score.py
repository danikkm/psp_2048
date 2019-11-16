# Score.py


class Score:
    __max_score = None
    __session_score = None

    def __init__(self, max_score, session_score):
        self.set_session_score(session_score)
        self.set_max_score(max_score)

    def sum_session_score(self, session_score):
        self.__session_score += session_score

    def set_session_score(self, session_score):
        self.__session_score = session_score

    def get_session_score(self):
        return self.__session_score

    def set_max_score(self, max_score):
        self.__max_score = max_score

    def get_max_score(self):
        return self.__max_score
