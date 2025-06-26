import tkinter as tk
import random


class GameInfo:
    def __init__(self):
        self.map = [0 for _ in range(9)]
        self.player_turn = random.randint(0, 1)


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


def draw_title(parent_frame):
    label = tk.Label(
        parent_frame,
        text="Game started!",
        fg="white",
        bg="black",
        font=("Arial", 24),
    )
    label.pack(pady=(20, 10))


def game(app):
    game_info = GameInfo()
    frame = tk.Frame(app.window, bg="black")
    frame.pack(expand=True, fill="both")
    app.content_frame = frame

    draw_title(frame)
    draw_grid(frame, game_info)


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
