# Main.py


import time

from Movement import Movement
from SystemHelper import SystemHelper


def main():
    # board = GameBoard(32, 4)
    # todo: rename and extract Movement class
    # todo: extract GameBoard class 
    board = Movement(32, 0, 4)

    # board.place_random_element()

    board.place_random_element()

    print("Controls: capital/non-capital WSAD letter or arrows")
    print("To exit the game press: q")

    # board.draw_game_board()

    board.draw_game_board()

    key_strokes = SystemHelper.get_key_strokes()

    print("Your current score is: ", board.score.get_session_score())

    while True:
        pressed_key = board.get_pressed_key()

        if pressed_key == list(key_strokes.values())[0] or \
                pressed_key == list(key_strokes.values())[4] or \
                pressed_key == list(key_strokes.values())[9]:
            board.movement_swipe_up()
            print("Your current score is: ", board.score.get_session_score())

        elif pressed_key == list(key_strokes.values())[1] or \
                pressed_key == list(key_strokes.values())[5] or \
                pressed_key == list(key_strokes.values())[10]:
            board.movement_swipe_down()
            print("Your current score is: ", board.score.get_session_score())
        elif pressed_key == list(key_strokes.values())[2] or \
                pressed_key == list(key_strokes.values())[6] or \
                pressed_key == list(key_strokes.values())[11]:
            board.movement_swipe_left()
            print("Your current score is: ", board.score.get_session_score())
        elif pressed_key == list(key_strokes.values())[3] or \
                pressed_key == list(key_strokes.values())[7] or \
                pressed_key == list(key_strokes.values())[12]:
            board.movement_swipe_right()
            print("Your current score is: ", board.score.get_session_score())
        elif pressed_key == list(key_strokes.values())[8]:
            quit()
        else:
            SystemHelper.flush_screen()
            print("Wrong key")
            board.draw_game_board()

        if board.game_over():
            time.sleep(1)
            print("Game over!")
            print("Restart game? (y/n)")
            time.sleep(1.5)
            if board.get_pressed_key() == 121:
                SystemHelper.flush_screen()
                main()
            else:
                quit()
        elif board.reached_max_score():
            print("You WON and reached: ", board.score.get_max_score())
            print("Restart game? (y/n)")
            time.sleep(1.5)
            if board.get_pressed_key() == 121:
                SystemHelper.flush_screen()
                main()
            else:
                quit()


if __name__ == '__main__':
    SystemHelper.flush_screen()
    main()
