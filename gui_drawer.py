# gui_drawer.py

from tkinter import *

from gui import GUI


class GUIDrawer:

    def __init__(self, size):
        self.size = size
        try:
            self.gui, self.GUI_runnable, = None, None
        except ImportError:
            self.gui, self.GUI_runnable, = False, False

    def enable_gui(self):
        if self.GUI_runnable is None:
            try:
                root = Tk()
                self.gui = GUI(root, self.size)
                self.GUI_runnable = True

            except E:
                self.GUI_runnable = False

    def is_gui_runnable(self):
        return self.GUI_runnable

    def get_gui(self):
        return self.gui
