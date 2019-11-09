# Main.py


import time

from GameBoard import GameBoard
from Movement import Movement
from Score import Score
from SystemHelper import SystemHelper


def main():
    board = GameBoard(4)

    board.place_random_element()

    print("Controls: capital/non-capital WSAD letter or arrows")
    print("To exit the game press: q")

    board.draw_game_board()

    key_strokes = SystemHelper.get_key_strokes()

    print("Your current score is: ", Score.get_score())

    while True:
        pressed_key = Movement.get_pressed_key()

        if pressed_key == list(key_strokes.values())[0] or \
                pressed_key == list(key_strokes.values())[4] or \
                pressed_key == list(key_strokes.values())[9]:
            Movement.movement_swipe_up(board)
            print("Your current score is: ", Score.get_score())

        elif pressed_key == list(key_strokes.values())[1] or \
                pressed_key == list(key_strokes.values())[5] or \
                pressed_key == list(key_strokes.values())[10]:
            Movement.movement_swipe_down(board)
            print("Your current score is: ", Score.get_score())
        elif pressed_key == list(key_strokes.values())[2] or \
                pressed_key == list(key_strokes.values())[6] or \
                pressed_key == list(key_strokes.values())[11]:
            Movement.movement_swipe_left(board)
            print("Your current score is: ", Score.get_score())
        elif pressed_key == list(key_strokes.values())[3] or \
                pressed_key == list(key_strokes.values())[7] or \
                pressed_key == list(key_strokes.values())[12]:
            Movement.movement_swipe_right(board)
            print("Your current score is: ", Score.get_score())
        elif pressed_key == list(key_strokes.values())[8]:
            quit()
        else:
            SystemHelper.flush_screen()
            print("Wrong key")
            board.draw_game_board()

        if Movement.game_over(board):
            time.sleep(1)
            print("Game over!")
            print("Restart game? (y/n)")
            time.sleep(1.5)
            if Movement.get_pressed_key() == 121:
                SystemHelper.flush_screen()
                main()
            else:
                quit()


if __name__ == '__main__':
    SystemHelper.flush_screen()
    main()
