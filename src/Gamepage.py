import tkinter as tk
from PIL import Image, ImageTk
from .Game.hooks import setup_game_events
from .Game.draws import draw_grid, draw_title
from .Game.menu_button import menu_button
import random


class GameInfo:
    def __init__(self, app):
        self.app = app
        scale = app.get_window_scale()
        image_size = max(int(100 * scale), 60)

        img1 = Image.open("sprites/boba.png").resize(
            (image_size, image_size), Image.Resampling.LANCZOS
        )
        img2 = Image.open("sprites/black_boba.png").resize(
            (image_size, image_size), Image.Resampling.LANCZOS
        )

        img1_transparent = img1.copy()
        img1_transparent.putalpha(128)
        img2_transparent = img2.copy()
        img2_transparent.putalpha(128)

        self.map = [0 for _ in range(9)]
        self.player_turn = random.randint(0, 1)
        self.rect_coords = []
        self.image_ids = [None] * 9
        self.hover_image_id = None
        self.turn_label = None
        self.game_ended = False
        self.play_again_button = None

        self.player1 = ImageTk.PhotoImage(img1)
        self.player2 = ImageTk.PhotoImage(img2)
        self.player1_transparent = ImageTk.PhotoImage(img1_transparent)
        self.player2_transparent = ImageTk.PhotoImage(img2_transparent)

    def get_responsive_font_size(self, base_size):
        """Calcule la taille de police responsive pour ce GameInfo"""
        scale = self.app.get_window_scale()
        return max(int(base_size * scale), 12)

    def update_turn_label(self):
        if self.turn_label is not None:
            font_size = self.get_responsive_font_size(22)
            if self.player_turn == 0:
                self.turn_label.config(
                    text="🧋 Boba turn! 🧋",
                    fg="#FF69B4",
                    font=("Comic Sans MS", font_size, "bold"),
                )
            else:
                self.turn_label.config(
                    text="⚫ Black boba turn! ⚫",
                    fg="#4B0082",
                    font=("Comic Sans MS", font_size, "bold"),
                )

    def update_map(self, i, current_player):
        if current_player == 0:
            self.map[i] = 1
        else:
            self.map[i] = 2


def game(app):
    game_info = GameInfo(app)
    frame = tk.Frame(app.window, bg="#87CEEB")
    frame.pack(expand=True, fill="both")
    app.content_frame = frame
    draw_title(frame, game_info)
    canvas = draw_grid(frame, game_info)
    setup_game_events(canvas, game_info, app)


def build_gamepage(app):
    game(app)
    menu_button(app)
    return app.content_frame
