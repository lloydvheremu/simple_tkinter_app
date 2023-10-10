# This is a sample Python script.

import tkinter as tk
from tkinter import ttk

import sv_ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("350x200")
        self.root.title("Text App")
        self.mainframe = tk.Frame(self.root)
        self.mainframe.pack(fill=tk.BOTH, expand=True)

        # set theme
        sv_ttk.use_dark_theme(self.root)
        # ***********WIDGETS***********
        # Label widget
        self.text = ttk.Label(self.mainframe, text="Hello World", font=('Brass Mono', 30))
        self.text.grid(row=0, column=0)

        # Entry widget
        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=1, column=0, pady=10, sticky='NWES')

        # Button widget FOR SET TEXT
        set_text_button = ttk.Button(self.mainframe, text="Set Text", command=self.set_text)
        set_text_button.grid(row=1, column=1, pady=10)

        # Combobox widget
        color_options = ['red', 'blue', 'green']
        self.set_color_field = ttk.Combobox(self.mainframe, values=color_options)
        self.set_color_field.grid(row=2, column=0, pady=10, sticky='NWES')
        # Button widget FOR COLOR
        set_color_button = ttk.Button(self.mainframe, text="Set Color", command=self.set_color)
        set_color_button.grid(row=2, column=1, pady=10)
        # Button widget FOR REVERSE
        self.reverse_text = ttk.Button(self.mainframe, text="Reverse Text", command=self.reverse)
        self.reverse_text.grid(row=3, column=0, pady=10, sticky='NWES')

        # ***********END WIDGETS***********

        self.root.mainloop()
        return

    def set_text(self):
        print("Setting text")
        newtext = self.set_text_field.get()
        self.text.config(text=newtext)

    def set_color(self):
        newcolor = self.set_color_field.get()
        self.text.config(foreground=newcolor)

    def reverse(self):
        newtext = self.text.cget("text")
        newtext = newtext[::-1]
        self.text.config(text=newtext)




if __name__ == "__main__":
    App()
