import tkinter as tk
from src.Homepage import homepage
from src.Gamepage import gamepage

game_state = 0
content_frame = None


def create_window():
    window = tk.Tk()
    window.config(bg="grey")
    window.title("TicTacToe Boba")
    window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
    return window


def clear_content():
    global content_frame
    if content_frame:
        content_frame.destroy()
        content_frame = None


def set_game_state(value, window):
    global game_state, content_frame
    game_state = value
    print(f"Game state changed to {game_state}")
    clear_content()

    if game_state == 0:
        content_frame = homepage(window, set_game_state)
    elif game_state == 1:
        content_frame = gamepage(set_game_state, window)


def main():
    window = create_window()
    set_game_state(0, window)
    window.mainloop()


if __name__ == "__main__":
    main()
