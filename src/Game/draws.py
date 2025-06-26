import tkinter as tk


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

    # Create a single label for turn display and store it in game_info
    game_info.turn_label = tk.Label(
        parent_frame,
        text="",
        fg="white",
        bg="black",
        font=("Arial", 24),
    )
    game_info.turn_label.pack(pady=(20, 10))

    # Update the turn label text
    game_info.update_turn_label()
