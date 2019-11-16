# SystemHelper.py
import os


class SystemHelper:

    def __init__(self):
        pass

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
            "upArrow": 65,
            "downArrow": 66,
            "leftArrow": 68,
            "rightArrow": 67,
            "q": 113,
            "Q": 81,
            "y": 121

        }

    def pressed_key(self, pressed_key):

        if pressed_key == self.get_key_strokes().get("W") or \
                pressed_key == self.get_key_strokes().get("w") or \
                pressed_key == self.get_key_strokes().get("upArrow"):
            return "UP"
        if pressed_key == self.get_key_strokes().get("S") or \
                pressed_key == self.get_key_strokes().get("s") or \
                pressed_key == self.get_key_strokes().get("downArrow"):
            return "DOWN"
        if pressed_key == self.get_key_strokes().get("A") or \
                pressed_key == self.get_key_strokes().get("a") or \
                pressed_key == self.get_key_strokes().get("leftArrow"):
            return "LEFT"
        if pressed_key == self.get_key_strokes().get("D") or \
                pressed_key == self.get_key_strokes().get("d") or \
                pressed_key == self.get_key_strokes().get("rightArrow"):
            return "RIGHT"
        if pressed_key == self.get_key_strokes().get("Q") or \
                pressed_key == self.get_key_strokes().get("q"):
            return "QUIT"
