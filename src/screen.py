import tkinter as tk
import tkinter.font as tk_font


class Screen(tk.Label):

    def __init__(self, parent, **kwargs):
        tk.Label.__init__(self, parent, **kwargs)

        # Configure the default Canvas for the screen
        if ('background' not in kwargs.keys() and
                'bg' not in kwargs.keys()):
            self.configure(bg='white')
        if ('borderwidth' not in kwargs.keys() and
                'bd' not in kwargs.keys()):
            self.configure(bd=2)
        if 'relief' not in kwargs.keys():
            self.configure(relief=tk.RIDGE)
        if 'anchor' not in kwargs.keys():
            self.configure(anchor='e')
        if 'font' not in kwargs.keys():
            self.configure(font=tk_font.Font(family='Gill Sans Nova', size=36))

        # Attributes
        self.expression = ""
        self.undo_list = []
        self.max_undo_length = 100

    def add_to_expression(self, string):
        if len(self.undo_list) == 100:
            del self.undo_list[0]
        self.undo_list.append(self.expression)
        self.expression += string
        self.configure(text=self.expression)

    def undo(self):
        self.expression = self.undo_list.pop()
        self.configure(text=self.expression)

    def clear(self):
        if len(self.undo_list) == 100:
            del self.undo_list[0]
        self.undo_list.append(self.expression)
        self.expression = ""
        self.configure(text=self.expression)

    def negate(self):
        if len(self.undo_list) == 100:
            del self.undo_list[0]
        self.undo_list.append(self.expression)
        self.expression = '-(' + self.expression + ')'
        self.configure(text=self.expression)

    def result(self, result):
        if len(self.undo_list) == 100:
            del self.undo_list[0]
        self.undo_list.append(self.expression)
        self.expression = result
        self.configure(text=self.expression)
