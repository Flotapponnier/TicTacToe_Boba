import tkinter as tk
from src.Homepage import build_homepage
from src.Gamepage import build_gamepage


class TicTacToeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TicTacToe Boba")
        self.window.config(bg="grey")
        self.window.geometry(
            f"{self.window.winfo_screenwidth()}x{self.window.winfo_screenheight()}"
        )

        # Game state
        self.game_state = 0
        self.content_frame = None

        # Homepage
        self.buttons_visible = False
        self.mode_buttons = {}

    def run(self):
        self.set_game_state(0)
        self.window.mainloop()

    def clear_content(self):
        if self.content_frame:
            self.content_frame.destroy()
            self.content_frame = None

    def set_game_state(self, new_state):
        self.game_state = new_state
        self.clear_content()

        if self.game_state == 0:
            self.content_frame = build_homepage(self)
        elif self.game_state == 1:
            self.content_frame = build_gamepage(self)


if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
