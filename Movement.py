from MovementSwipeDown import MovementSwipeDown
from MovementSwipeLeft import MovementSwipeLeft
from MovementSwipeRight import MovementSwipeRight
from MovementSwipeUp import MovementSwipeUp


class Movement:

    def __init__(self):
        pass

    @staticmethod
    def swipe_up(obj):
        return MovementSwipeUp.swipe(obj)

    @staticmethod
    def swipe_down(obj):
        return MovementSwipeDown.swipe(obj)

    @staticmethod
    def swipe_left(obj):
        return MovementSwipeLeft.swipe(obj)

    @staticmethod
    def swipe_right(obj):
        return MovementSwipeRight.swipe(obj)

