# gui.py

from tkinter import *


class GUI(Frame):
    def __init__(self, master, size):
        Frame.__init__(self, master)
        self.background_color = {'2': '#EBE1D8', '4': '#ECE0CB', '8': '#F4B177', '16': '#F7975D', '32': '#FA7962',
                                 '64': '#F2613D', '128': '#EBE898', '256': '#F0D068', '512': '#EBE546',
                                 '1024': '#EAC80D', '2048': '#F4FC08', '4096': '#A4FC0D', '8192': '#FC0D64'}
        self.foreground_color = {'2': '#857865', '4': '#857865', '8': '#FDF5E9', '16': '#FDF5E9', '32': '#FDF5E9',
                                 '64': '#FDF5E9', '128': '#FDF5E9', '256': '#FDF5E9', '512': '#FDF5E9',
                                 '1024': '#FDF5E9', '2048': '#FDF5E9', '4096': '#FDF5E9', '8192': '#FDF5E9'}
        self.grid(sticky=N + S + E + W)

        self.board_size = size
        self.matrix_numbers = []
        self.create_grid(self.board_size)

    def create_grid(self, board_size):
        frame = Frame(self, width=500, height=500, bg='#827970', borderwidth=5)
        frame.grid(sticky=N + S + E + W)
        for i in range(int(board_size)):
            label_row = []
            for j in range(int(board_size)):
                frames = Frame(frame, bg='#EEE4DB', height=150, width=150, relief=SUNKEN)
                frames.grid(row=i, column=j, padx=5, pady=5, sticky=N + S + E + W)
                label = Label(frame, text="", background="#D6CDC5", font=("Helvetica", 60), justify=CENTER)
                label.grid(row=i, column=j, padx=5, pady=5, sticky=N + S + E + W)
                label_row.append(label)
            self.matrix_numbers.append(label_row)

    def update_grid(self, board):
        assert len(board) == self.board_size
        for x in range(len(board)):
            for y in range(len(board)):
                if board[x][y] == '*':
                    self.matrix_numbers[x][y].configure(text='', bg='#EEE4DB')
                else:
                    self.matrix_numbers[x][y].configure(text=str(board[x][y]), bg=self.background_color[board[x][y]],
                                                        fg=self.foreground_color[board[x][y]])
