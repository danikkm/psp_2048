# main.py

import time

from game import Game
from system_helper import SystemHelper


def main():
    game = Game(2048, 4)
    system_helper = SystemHelper()

    game.board.place_random_element()

    print("Controls: capital/non-capital WSAD letter or arrows")
    print("To exit the game press: q")

    game.board.draw_game_board()

    while True:
        print("Your current score is: ", game.score.get_session_score())

        pressed_key = game.get_pressed_key()

        game.swipe(pressed_key)

        if game.game_over():
            print("Game over!")
            print("Restart game? (y/n)")
            time.sleep(1)
            if game.get_pressed_key() == system_helper.set_key_strokes().get("y"):
                system_helper.flush_screen()
                main()
            else:
                quit()
        elif game.reached_max_score():
            print("You WON and reached: ", game.score.get_max_score())
            print("Restart game? (y/n)")
            time.sleep(1)
            if game.get_pressed_key() == system_helper.set_key_strokes().get("y"):
                system_helper.flush_screen()
                main()
            else:
                quit()


if __name__ == '__main__':
    SystemHelper.flush_screen()
    main()
