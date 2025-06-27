import tkinter as tk
import os
from src.Homepage import build_homepage
from src.Gamepage import build_gamepage
from src.pearl_animation import PearlAnimation
from src.background_music import BackgroundMusicManager


class TicTacToeApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TicTacToe Boba")
        self.window.config(bg="#87CEEB")

        self.setup_responsive_window()

        icon_path = os.path.join("sprites", "boba.png")
        try:
            icon = tk.PhotoImage(file=icon_path)
            self.window.iconphoto(False, icon)
        except Exception as e:
            print(f"Error loading icon: {e}")

        self.game_state = 0
        self.type_game = 0
        self.content_frame = None
        self.buttons_visible = False
        self.mode_buttons = {}
        self.pearl_animation = PearlAnimation(self.window)

        self.music_manager = BackgroundMusicManager(volume=0.2)
        music_path = os.path.join("music", "retro_background.mp3")
        if self.music_manager.load_music(music_path):
            self.music_manager.play_music(loop=True)

        self.window.bind("<Configure>", self.on_window_resize)

    def setup_responsive_window(self):
        self.window.minsize(800, 600)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        initial_width = int(screen_width * 0.8)
        initial_height = int(screen_height * 0.8)

        x = (screen_width - initial_width) // 2
        y = (screen_height - initial_height) // 2

        self.window.geometry(f"{initial_width}x{initial_height}+{x}+{y}")

        self.window.resizable(True, True)

    def on_window_resize(self, event):
        if event.widget == self.window:
            if hasattr(self, "pearl_animation") and self.pearl_animation.running:
                pass

    def get_window_scale(self):
        """Calcule le facteur d'échelle basé sur la taille de la fenêtre"""
        base_width = 1200
        base_height = 800

        current_width = self.window.winfo_width()
        current_height = self.window.winfo_height()

        if current_width <= 1 or current_height <= 1:
            return 1.0

        scale_x = current_width / base_width
        scale_y = current_height / base_height

        return min(scale_x, scale_y, 1.5)

    def run(self):
        self.set_game_state(0, 0)
        self.window.mainloop()

    def clear_content(self):
        if self.content_frame:
            self.pearl_animation.stop_animation()
            self.content_frame.destroy()
            self.content_frame = None

    def set_game_state(self, new_state, type_game=None):
        self.game_state = new_state
        if type_game is not None:
            self.type_game = type_game
        if new_state == 0:
            self.type_game = 0

        self.clear_content()
        if self.game_state == 0:
            self.content_frame = build_homepage(self)
            self.pearl_animation.start_animation(self.content_frame)
        elif self.game_state == 1:
            self.content_frame = build_gamepage(self)
            self.pearl_animation.start_animation(self.content_frame)

    def __del__(self):
        if hasattr(self, "music_manager"):
            self.music_manager.cleanup()


if __name__ == "__main__":
    app = TicTacToeApp()
    app.run()
