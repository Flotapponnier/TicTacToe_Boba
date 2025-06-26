import tkinter as tk
import os
from src.Homepage import build_homepage
from src.Gamepage import build_gamepage
from src.pearl_animation import PearlAnimation


class TicTacToeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TicTacToe Boba")
        self.window.config(bg="#87CEEB")
        self.window.geometry(
            f"{self.window.winfo_screenwidth()}x{self.window.winfo_screenheight()}"
        )

        icon_path = os.path.join("sprites", "boba.png")
        try:
            icon = tk.PhotoImage(file=icon_path)
            self.window.iconphoto(False, icon)
        except Exception as e:
            print(f"Error loading icon: {e}")

        self.game_state = 0
        self.content_frame = None
        self.buttons_visible = False
        self.mode_buttons = {}
        self.pearl_animation = PearlAnimation(self.window)

    def run(self):
        self.set_game_state(0)
        self.window.mainloop()

    def clear_content(self):
        if self.content_frame:
            self.pearl_animation.stop_animation()
            self.content_frame.destroy()
            self.content_frame = None

    def set_game_state(self, new_state):
        self.game_state = new_state
        self.clear_content()

        if self.game_state == 0:
            self.content_frame = build_homepage(self)
            self.pearl_animation.start_animation(self.content_frame)
        elif self.game_state == 1:
            self.content_frame = build_gamepage(self)
            self.pearl_animation.start_animation(self.content_frame)


if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
