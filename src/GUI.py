import tkinter as tk
from src.library import Library

class GUI:
    def __init__(self, master):
        self.master = master
        self.library = Library()
        self.create_window()
        self.create_mainpage()

    def create_window(self):
        self.master.title("Game Manager")
        self.master.geometry("800x600")
        self.master.configure(background = "gray")

    def create_mainpage(self):
        self.button1 = tk.Button(self.master, text="Click Me!", command=lambda: self.library.method('Clicked')).pack()
        self.entry1 = tk.Entry(self.master, justify='center').pack()
