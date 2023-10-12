# This is a sample Python script.

import tkinter as tk
from tkinter import ttk
from windowsTheme import get_current_theme

import sv_ttk
import winreg


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.theme = get_current_theme()
        self.root.geometry("400x400")
        self.root.title("Text App")
        self.mainframe = tk.Frame(self.root)
        self.mainframe.pack(fill=tk.BOTH, expand=True)

        # set theme
        # sv_ttk.use_dark_theme(self.root)
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

        # Button widget FOR THEME
        self.theme_button = ttk.Button(self.mainframe, text="Set Theme", command=self.set_theme)
        self.theme_button.grid(row=3, column=1, pady=10, sticky='NWES')

        # RADIO BUTTONS FOR CHOOSING THEME
        self.selection = tk.StringVar(value="default")

        themes = ["System Theme", "Light", "Dark"]
        values = ["default", "light", "dark"]

        for i, theme in enumerate(themes):
            ttk.Radiobutton(
                self.mainframe,
                text=theme,
                variable=self.selection,
                command=self.set_theme(),
                value=values[i]
            ).grid(row=4, column=i, pady=10, sticky='NWES')

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

    def set_theme(self):
        print(self.selection.get())
        if self.selection.get() == "light":
            sv_ttk.use_light_theme(self.root)
            return
        elif self.selection.get() == "dark":
            sv_ttk.use_dark_theme(self.root)
            return
        else:
            sv_ttk.set_theme(get_current_theme())
            return


if __name__ == "__main__":
    print(__name__)
    App()
