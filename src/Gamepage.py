import tkinter as tk
from PIL import Image, ImageTk
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


def draw_grid(parent_frame, game_info):
    rect_size = 100
    center_frame = tk.Frame(parent_frame, bg="black")
    center_frame.pack(expand=True)
    canvas = tk.Canvas(
        center_frame,
        width=300,
        height=300,
        bg="black",
        highlightthickness=0,
    )
    canvas.pack()
    for i, value in enumerate(game_info.map):
        row = i // 3
        col = i % 3
        x1 = col * rect_size
        y1 = row * rect_size
        x2 = x1 + rect_size
        y2 = y1 + rect_size
        color = "white" if value == 0 else "grey"
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
        game_info.rect_coords.append((x1, y1, x2, y2))
    return canvas


def draw_title(parent_frame, game_info):
    label = tk.Label(
        parent_frame,
        text="Game started!",
        fg="white",
        bg="black",
        font=("Arial", 24),
    )
    label.pack(pady=(20, 10))

    boba_turn = tk.Label(
        parent_frame,
        text="Bobanou turn !",
        fg="white",
        bg="black",
        font=("Arial", 24),
    )
    black_boba_turn = tk.Label(
        parent_frame,
        text="Black boba turn !",
        fg="white",
        bg="black",
        font=("Arial", 24),
    )
    if game_info.player_turn == 0:
        boba_turn.pack(pady=(20, 10))
    else:
        black_boba_turn.pack(pady=(20, 10))


def check_hooks(canvas, game_info):
    game_info.hover_image_id = None

    def on_click(event):
        if game_info.hover_image_id is not None:
            canvas.delete(game_info.hover_image_id)
            game_info.hover_image_id = None

        for i, (x1, y1, x2, y2) in enumerate(game_info.rect_coords):
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                if game_info.map[i] == 0:
                    game_info.map[i] = 1
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2
                    if game_info.player_turn == 0:
                        img_id = canvas.create_image(cx, cy, image=game_info.player1)
                        game_info.image_ids[i] = img_id
                        game_info.player_turn = 1
                    else:
                        img_id = canvas.create_image(cx, cy, image=game_info.player2)
                        game_info.image_ids[i] = img_id
                        game_info.player_turn = 0
                break

    def on_motion(event):

        hovered_index = None
        for i, (x1, y1, x2, y2) in enumerate(game_info.rect_coords):
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                hovered_index = i
                break

        if game_info.hover_image_id is not None:
            canvas.delete(game_info.hover_image_id)
            game_info.hover_image_id = None

        if hovered_index is not None and game_info.map[hovered_index] == 0:
            x1, y1, x2, y2 = game_info.rect_coords[hovered_index]
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            if game_info.player_turn == 0:
                hover_image = game_info.player1_transparent
            else:
                hover_image = game_info.player2_transparent
            game_info.hover_image_id = canvas.create_image(cx, cy, image=hover_image)

    def on_leave(event):
        if game_info.hover_image_id is not None:
            canvas.delete(game_info.hover_image_id)
            game_info.hover_image_id = None

    canvas.bind("<Button-1>", on_click)
    canvas.bind("<Motion>", on_motion)
    canvas.bind("<Leave>", on_leave)


def game(app):
    game_info = GameInfo()
    frame = tk.Frame(app.window, bg="black")
    frame.pack(expand=True, fill="both")
    app.content_frame = frame
    draw_title(frame, game_info)
    canvas = draw_grid(frame, game_info)
    check_hooks(canvas, game_info)


def menu_button(app):
    menu_btn = tk.Button(
        app.content_frame,
        text="Return to menu",
        fg="white",
        bg="black",
        font=("Arial", 24),
        command=lambda: app.set_game_state(0),
    )
    menu_btn.pack(side="bottom", pady=20)


def build_gamepage(app):
    game(app)
    menu_button(app)
    return app.content_frame
