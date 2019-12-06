# Main.py


import time

from Game import Game
from SystemHelper import SystemHelper


def main():
    # todo: add ability to set max score dynamically
    # todo: allow only numbers power of 2
    # todo: fix controls when using arrows
    game = Game(1024, 0, 4)
    system_helper = SystemHelper()

    game.board.place_random_element()

    print("Controls: capital/non-capital WSAD letter or arrows")
    print("To exit the game press: q")

    game.board.draw_game_board()

    while True:
        print("Your current score is: ", game.score.get_session_score())
        pressed_key = game.get_pressed_key()

        if system_helper.pressed_key(pressed_key) == "UP":
            game.movement_swipe_up()

        elif system_helper.pressed_key(pressed_key) == "DOWN":
            game.movement_swipe_down()
        elif system_helper.pressed_key(pressed_key) == "LEFT":
            game.movement_swipe_left()
        elif system_helper.pressed_key(pressed_key) == "RIGHT":
            game.movement_swipe_right()
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
