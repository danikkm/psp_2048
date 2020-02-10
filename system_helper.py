# system_helper.py

import os


class SystemHelper:
    key_dict = {}

    def __init__(self):
        self.key_dict = self.set_key_strokes()

    @staticmethod
    def flush_screen():
        try:
            try:
                os.system('clear')
            except NameError:
                os.system('cls')
        except NameError:
            print('\n' * 80)

    # TODO: fix wrong getch code
    @staticmethod
    def set_key_strokes():
        return {
            "W": 87,
            "S": 83,
            "A": 65,
            "D": 68,
            "w": 119,
            "s": 115,
            "a": 97,
            "d": 100,
            "upArrow": 65,
            "downArrow": 66,
            "leftArrow": 68,
            "rightArrow": 67,
            "q": 113,
            "Q": 81,
            "y": 121,
            "n": 110

        }

    def pressed_key(self, pressed_key):

        if pressed_key == self.key_dict.get("W") or \
                pressed_key == self.key_dict.get("w") or \
                pressed_key == self.key_dict.get("upArrow"):
            return "UP"
        if pressed_key == self.key_dict.get("S") or \
                pressed_key == self.key_dict.get("s") or \
                pressed_key == self.key_dict.get("downArrow"):
            return "DOWN"
        if pressed_key == self.key_dict.get("A") or \
                pressed_key == self.key_dict.get("a") or \
                pressed_key == self.key_dict.get("leftArrow"):
            return "LEFT"
        if pressed_key == self.key_dict.get("D") or \
                pressed_key == self.key_dict.get("d") or \
                pressed_key == self.key_dict.get("rightArrow"):
            return "RIGHT"
        if pressed_key == self.key_dict.get("Q") or \
                pressed_key == self.key_dict.get("q"):
            return "QUIT"
