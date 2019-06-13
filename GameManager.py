import tkinter as tk
from src.library import Library
from src.GUI import GUI

root = tk.Tk()
gui = GUI(root)
root.mainloop()

library = Library()