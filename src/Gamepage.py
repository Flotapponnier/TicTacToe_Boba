import tkinter as tk
from PIL import Image, ImageTk
from .Game.hooks import events_hooks
from .Game.draws import draw_grid, draw_title
from .Game.menu_button import menu_button
import random


class GameInfo:
    def __init__(self):
        # Load and resize sprites
        img1 = Image.open("sprites/boba.png").resize(
            (100, 100), Image.Resampling.LANCZOS
        )
        img2 = Image.open("sprites/black_boba.png").resize(
            (100, 100), Image.Resampling.LANCZOS
        )

        # Create transparent versions (50% opacity)
        img1_transparent = img1.copy()
        img1_transparent.putalpha(128)

        img2_transparent = img2.copy()
        img2_transparent.putalpha(128)

        # Game state initialization
        self.map = [0 for _ in range(9)]
        self.player_turn = random.randint(0, 1)
        self.rect_coords = []
        self.image_ids = [None] * 9
        self.hover_image_id = None

        # Normal images
        self.player1 = ImageTk.PhotoImage(img1)
        self.player2 = ImageTk.PhotoImage(img2)

        # Transparent images for hover preview
        self.player1_transparent = ImageTk.PhotoImage(img1_transparent)
        self.player2_transparent = ImageTk.PhotoImage(img2_transparent)


def game(app):
    game_info = GameInfo()
    frame = tk.Frame(app.window, bg="black")
    frame.pack(expand=True, fill="both")
    app.content_frame = frame
    draw_title(frame, game_info)
    canvas = draw_grid(frame, game_info)
    events_hooks(canvas, game_info)


def build_gamepage(app):
    game(app)
    menu_button(app)
    return app.content_frame
