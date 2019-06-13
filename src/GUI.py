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
        self.master.grid_columnconfigure(2, minsize=80)
        self.master.grid_rowconfigure(0, minsize=300)
        self.submit = tk.Button(self.master, text="Submit", command=lambda: self.library.method(self.title.get())).grid(row=2, column=3)
        self.title = tk.StringVar()
        self.title_label = tk.Label(self.master, background='gray', text='Title: ').grid(row=1, column=0)
        self.title_entry = tk.Entry(self.master, justify='center', textvariable=self.title).grid(row=1, column=1)
        self.console = tk.StringVar()
        self.console_label = tk.Label(self.master, background='gray', text='Console: ').grid(row=2, column=0)
        self.console_entry = tk.Entry(self.master, justify='center', textvariable=self.title).grid(row=2, column=1)
        self.status = tk.StringVar()
        self.status_label = tk.Label(self.master, background='gray', text='Status: ').grid(row=3, column=0)
        self.status_entry = tk.Entry(self.master, justify='center', textvariable=self.title).grid(row=3, column=1)

