# Movement.py

from MovementSwipeDown import MovementSwipeDown
from MovementSwipeLeft import MovementSwipeLeft
from MovementSwipeRight import MovementSwipeRight
from MovementSwipeUp import MovementSwipeUp


class Movement:

    @staticmethod
    def swipe(obj, pressed_key):
        try:
            if pressed_key == "UP":
                return MovementSwipeUp.swipe(obj, "UP")
            elif pressed_key == "DOWN":
                return MovementSwipeDown.swipe(obj, "DOWN")
            elif pressed_key == "LEFT":
                return MovementSwipeLeft.swipe(obj, "LEFT")
            elif pressed_key == "RIGHT":
                return MovementSwipeRight.swipe(obj, "RIGHT")
            elif pressed_key == "QUIT":
                quit()
            raise AssertionError("Wrong key")
        except AssertionError as _e:
            print(_e)
