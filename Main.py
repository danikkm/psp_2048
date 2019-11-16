# Main.py


import time

from Game import Game
from SystemHelper import SystemHelper


def main():
    game = Game(8, 0, 3)
    system_helper = SystemHelper()

    game.board.place_random_element()

    print("Controls: capital/non-capital WSAD letter or arrows")
    print("To exit the game press: q")

    game.board.draw_game_board()

    print("Your current score is: ", game.score.get_session_score())

    while True:
        pressed_key = game.get_pressed_key()

        if system_helper.pressed_key(pressed_key) == "UP":
            game.movement_swipe_up()
            print("Your current score is: ", game.score.get_session_score())

        elif system_helper.pressed_key(pressed_key) == "DOWN":
            game.movement_swipe_down()
            print("Your current score is: ", game.score.get_session_score())
        elif system_helper.pressed_key(pressed_key) == "LEFT":
            game.movement_swipe_left()
            print("Your current score is: ", game.score.get_session_score())
        elif system_helper.pressed_key(pressed_key) == "RIGHT":
            game.movement_swipe_right()
            print("Your current score is: ", game.score.get_session_score())
        elif system_helper.pressed_key(pressed_key) == "QUIT":
            quit()
        else:
            system_helper.flush_screen()
            print("Wrong key")
            game.board.draw_game_board()

        if game.game_over():
            print("Game over!")
            print("Restart game? (y/n)")
            time.sleep(1)
            if game.get_pressed_key() == system_helper.get_key_strokes().get("y"):
                system_helper.flush_screen()
                main()
            else:
                quit()
        elif game.reached_max_score():
            print("You WON and reached: ", game.score.get_max_score())
            print("Restart game? (y/n)")
            time.sleep(1)
            if game.get_pressed_key() == system_helper.get_key_strokes().get("y"):
                system_helper.flush_screen()
                main()
            else:
                quit()


if __name__ == '__main__':
    SystemHelper.flush_screen()
    main()
