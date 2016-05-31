import Tkinter as tk

class TaskView(tk.Toplevel):

    ''' Constructor '''
    def __init__(self, master):
        tk.Toplevel.__init__(self, master)
        self.protocol('WM_DELETE_WINDOW', self.master.destroy)
        self.master = master

        ''' Public attributes title and label '''
        self.__title_var = tk.StringVar()
        self.__title_label = tk.Label(self, textvariable=self.__title_var)

        ''' Align right '''
        self.__title_label.pack(side='right')

        ''' Toggle button reverse '''
        self.toggle_button = tk.Button(self, text="Reverse")
        self.toggle_button.pack(side='left')

    ''' Update title '''
    def update_title(self, title):
        self.__title_var.set(title)
