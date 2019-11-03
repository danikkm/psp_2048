# SystemHelper.py
import os


def flushScreen():
    try:
        try:
            os.system('clear')
        except:
            os.system('cls')
    except:
        print('\n' * 80)




