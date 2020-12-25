import tkinter
from tkinter import ttk
import os

class TreeWindows(tkinter.Frame):
    def __init__(self, master):
        frame = tkinter.Frame(master)
        frame.pack()

        self.tree = ttk.Treeview(frame)
        self.tree.pack()

