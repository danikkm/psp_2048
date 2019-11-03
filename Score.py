# Score.py

class Score:

    def __init__(self, score):
        self.setScore(score)

    @classmethod
    def setScore(self, score):
        self.__score = score

    @classmethod
    def getScore(self):
        return self.__score

    @classmethod
    def addScore(self, score):
        self.__score += score