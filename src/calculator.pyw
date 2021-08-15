from screen import *


class Calculator(tk.Tk):

    def __init__(self, **kwargs):
        tk.Tk.__init__(self, **kwargs)

        self.screen = Screen(self, width=17)
        self.screen.grid(row=0, column=0, columnspan=4, sticky='new')
        self.resizable(False, False)

        self.expression = ""
        self.undo_list = []
        self.memory = '0'

        tk.Button(self, relief='flat', background='#ff5753', fg='white', text='MC',
                  font=tk_font.Font(family='Gill Sans Nova', size=16, weight='bold'),
                  command=self.clear_memory).grid(row=1, column=0, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief='flat', background='#ff5753', fg='white', text='MR',
                  font=tk_font.Font(family='Gill Sans Nova', size=16, weight='bold'),
                  command=lambda: self.add_to_expression(self.memory)).grid(row=1, column=1, sticky='nesw',
                                                                            padx=2, pady=2)
        tk.Button(self, relief='flat', background='#ff5753', fg='white', text='MS',
                  font=tk_font.Font(family='Gill Sans Nova', size=16, weight='bold'),
                  command=self.store).grid(row=1, column=2, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief='flat', background='#ff5753', fg='white', text='←',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=self.undo).grid(row=1, column=3, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief='flat', background='#ff5753', fg='white', text='C',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=self.clear).grid(row=2, column=0, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='(',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('(')).grid(row=2, column=1, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text=')',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression(')')).grid(row=2, column=2, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief='flat', background='#ee7723', fg='white', text='=',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=self.evaluate).grid(row=2, column=3, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='7',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('7')).grid(row=3, column=0, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='8',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('8')).grid(row=3, column=1, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='9',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('9')).grid(row=3, column=2, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='4',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('4')).grid(row=4, column=0, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='5',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('5')).grid(row=4, column=1, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='6',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('6')).grid(row=4, column=2, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='1',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('1')).grid(row=5, column=0, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='2',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('2')).grid(row=5, column=1, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='3',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('3')).grid(row=5, column=2, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='+/-',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=self.negate).grid(row=6, column=0, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='0',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('0')).grid(row=6, column=1, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='.',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.add_to_expression('.')).grid(row=6, column=2, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background='#00ff08', text='/', fg='white',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=lambda: self.add_to_expression(' / ')).grid(row=3, column=3, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background='#00ff08', text='x', fg='white',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=lambda: self.add_to_expression(' * ')).grid(row=4, column=3, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background='#00ff08', text='-', fg='white',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=lambda: self.add_to_expression(' - ')).grid(row=5, column=3, sticky='nesw', padx=2, pady=2)
        tk.Button(self, relief="flat", background='#00ff08', text='+', fg='white',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=lambda: self.add_to_expression(' + ')).grid(row=6, column=3, sticky='nesw', padx=2, pady=2)

        self.bind('<BackSpace>', lambda event: self.undo())
        self.bind('<(>', lambda event: self.add_to_expression('('))
        self.bind('<)>', lambda event: self.add_to_expression(')'))
        self.bind('<Return>', lambda event: self.evaluate())
        self.bind('7', lambda event: self.add_to_expression('7'))
        self.bind('8', lambda event: self.add_to_expression('8'))
        self.bind('9', lambda event: self.add_to_expression('9'))
        self.bind('4', lambda event: self.add_to_expression('4'))
        self.bind('5', lambda event: self.add_to_expression('5'))
        self.bind('6', lambda event: self.add_to_expression('6'))
        self.bind('1', lambda event: self.add_to_expression('1'))
        self.bind('2', lambda event: self.add_to_expression('2'))
        self.bind('3', lambda event: self.add_to_expression('3'))
        self.bind('0', lambda event: self.add_to_expression('0'))
        self.bind('.', lambda event: self.add_to_expression('.'))
        self.bind('+', lambda event: self.add_to_expression(' + '))
        self.bind('-', lambda event: self.add_to_expression('-'))
        self.bind('*', lambda event: self.add_to_expression(' * '))
        self.bind('/', lambda event: self.add_to_expression(' / '))

    def add_to_expression(self, string):

        if len(self.expression) > 16:
            return
        if len(self.undo_list) == 100:
            del self.undo_list[0]
        if string == ' * ':
            self.screen.add_to_expression(' x ')
        else:
            self.screen.add_to_expression(string)

        self.undo_list.append(self.expression)
        self.expression += string

    def undo(self):
        self.screen.undo()
        self.expression = self.undo_list.pop()

    def clear(self):
        self.screen.clear()
        if len(self.undo_list) == 100:
            del self.undo_list[0]
        self.undo_list.append(self.expression)
        self.expression = ""

    def negate(self):
        self.screen.negate()
        if len(self.undo_list) == 100:
            del self.undo_list[0]
        self.undo_list.append(self.expression)
        self.expression = "-(" + self.expression + ")"

    def evaluate(self):
        if len(self.undo_list) == 100:
            del self.undo_list[0]
        self.undo_list.append(self.expression)
        temp = eval(self.expression)
        if temp > 1e15:
            self.expression = '{:16e}'.format(temp)
        else:
            self.expression = str(temp)
        self.screen.result(self.expression)

    def store(self):
        self.memory = str(eval(self.expression))

    def clear_memory(self):
        self.memory = '0'


Calculator().mainloop()
