

class Calculator(tk.Tk):

    def __init__(self, **kwargs):
        tk.Tk.__init__(self, **kwargs)

        self.screen = Screen(self, width=17)
        self.screen.grid(row=0, column=0, columnspan=4, sticky='new')
        self.resizable(False, False)

        tk.Button(self, relief='flat', background='#ff5753', fg='white', text='C',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'), command=self.screen.clear).grid(
            row=1, column=0,
            columnspan=2,
            sticky='nesw', padx=2,
            pady=2)
        tk.Button(self, relief='flat', background='#ff5753', fg='white', text='←',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'), command=self.screen.undo).grid(
            row=1, column=2,
            columnspan=2,
            sticky='nesw', padx=2,
            pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='7',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('7')).grid(row=2, column=0,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='8',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('8')).grid(row=2, column=1,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='9',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('9')).grid(row=2, column=2,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='4',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('4')).grid(row=3, column=0,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='5',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('5')).grid(row=3, column=1,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='6',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('6')).grid(row=3, column=2,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='1',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('1')).grid(row=4, column=0,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='2',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('2')).grid(row=4, column=1,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='3',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('3')).grid(row=4, column=2,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='0',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('0')).grid(row=5, column=0,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief="flat", background="#ccc", text='.',
                  font=tk_font.Font(family='Gill Sans Nova', size=20),
                  command=lambda: self.screen.add_to_expression('.')).grid(row=5, column=1,
                                                                           sticky='nesw', padx=2,
                                                                           pady=2)
        tk.Button(self, relief='flat', background='#ee7723', fg='white', text='=',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=self.screen.evaluate).grid(row=5, column=2,
                                                     sticky='nesw',
                                                     padx=2, pady=2)
        tk.Button(self, relief="flat", background='#00ff08', text='/', fg='white',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=lambda: self.screen.add_to_expression(' / ')).grid(row=2, column=3,
                                                                             sticky='nesw',
                                                                             padx=2, pady=2)
        tk.Button(self, relief="flat", background='#00ff08', text='x', fg='white',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=lambda: self.screen.add_to_expression(' * ')).grid(row=3, column=3,
                                                                             sticky='nesw',
                                                                             padx=2, pady=2)
        tk.Button(self, relief="flat", background='#00ff08', text='-', fg='white',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=lambda: self.screen.add_to_expression(' - ')).grid(row=4, column=3,
                                                                             sticky='nesw',
                                                                             padx=2, pady=2)
        tk.Button(self, relief="flat", background='#00ff08', text='+', fg='white',
                  font=tk_font.Font(family='Gill Sans Nova', size=20, weight='bold'),
                  command=lambda: self.screen.add_to_expression(' + ')).grid(row=5, column=3,
                                                                             sticky='nesw',
                                                                             padx=2, pady=2)