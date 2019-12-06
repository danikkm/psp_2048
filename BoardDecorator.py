class BoardDecorator:
    __board_colors = None

    def __init__(self):
        self.__board_colors = self.set_board_colors()

    @staticmethod
    def set_board_colors():
        return {
            '*': None,
            '2': 'red',
            '4': 'yellow',
            '8': 'green',
            '16': 'magenta',
            '32': 'cyan',
            '64': 'blue',
            '128': 'magenta',
            '256': 'white',
            '512': 'green',
            '1024': 'blue',
            '2048': 'red'
        }

    def get_board_colors(self):
        return self.__board_colors
