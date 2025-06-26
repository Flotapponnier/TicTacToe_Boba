import tkinter as tk


def draw_grid(parent_frame, game_info):
    rect_size = 100
    center_frame = tk.Frame(parent_frame, bg="#87CEEB")
    center_frame.pack(expand=True)
    canvas = tk.Canvas(
        center_frame,
        width=320,
        height=320,
        bg="#87CEEB",
        highlightthickness=0,
    )
    canvas.pack()

    for i, value in enumerate(game_info.map):
        row = i // 3
        col = i % 3
        x1 = col * rect_size + 10
        y1 = row * rect_size + 10
        x2 = x1 + rect_size
        y2 = y1 + rect_size

        if (row + col) % 2 == 0:
            color = "#FFFFFF"
        else:
            color = "#F0F8FF"

        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#4169E1", width=3)
        game_info.rect_coords.append((x1, y1, x2, y2))

    return canvas


def draw_title(parent_frame, game_info):
    label = tk.Label(
        parent_frame,
        text="🎮 Game started! 🎮",
        fg="#FF4500",
        bg="#87CEEB",
        font=("Comic Sans MS", 28, "bold"),
        pady=10,
    )
    label.pack(pady=(20, 10))

    game_info.turn_label = tk.Label(
        parent_frame,
        text="",
        fg="#FF69B4",
        bg="#87CEEB",
        font=("Comic Sans MS", 22, "bold"),
        pady=5,
    )
    game_info.turn_label.pack(pady=(10, 20))

    game_info.update_turn_label()
