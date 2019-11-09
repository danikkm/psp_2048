# SystemHelper.py
import os


class SystemHelper:

    @staticmethod
    def flush_screen():
        try:
            try:
                os.system('clear')
            except:
                os.system('cls')
        except:
            print('\n' * 80)

    @staticmethod
    def get_key_strokes():
        return {
            "W": 87,
            "S": 83,
            "A": 65,
            "D": 68,
            "w": 119,
            "s": 115,
            "a": 97,
            "d": 100,
            "q": 113,
            "upArrow": 65,
            "downArrow": 66,
            "leftArrow": 68,
            "rightArrow": 67
        }
