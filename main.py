import tkinter as tk
from tkinter import ttk


def create_window():
    window = tk.Tk()
    window.config(bg="grey")
    window.title("TicTacToe Boba")

    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry(f"{width}x{height}")
    return window


def homepage(window):
    button = tk.Button(window, text="Play Tic Tac Toe")
    button.pack()


def main():
    window = create_window()
    homepage(window)
    window.mainloop()


main()
