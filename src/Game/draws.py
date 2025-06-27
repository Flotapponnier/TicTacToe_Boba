import tkinter as tk


def draw_grid(parent_frame, game_info):
    scale = game_info.app.get_window_scale()
    rect_size = max(int(100 * scale), 80)
    canvas_size = rect_size * 3 + 20

    center_frame = tk.Frame(parent_frame, bg="#87CEEB")
    center_frame.pack(expand=True)

    canvas = tk.Canvas(
        center_frame,
        width=canvas_size,
        height=canvas_size,
        bg="#87CEEB",
        highlightthickness=0,
    )
    canvas.pack()

    game_info.rect_coords.clear()

    border_width = max(int(3 * scale), 2)

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

        canvas.create_rectangle(
            x1, y1, x2, y2, fill=color, outline="#4169E1", width=border_width
        )
        game_info.rect_coords.append((x1, y1, x2, y2))

    return canvas


def draw_title(parent_frame, game_info):
    title_font_size = game_info.get_responsive_font_size(28)
    title_pady = max(int(10 * game_info.app.get_window_scale()), 5)

    label = tk.Label(
        parent_frame,
        text="🎮 Game started! 🎮",
        fg="#FF4500",
        bg="#87CEEB",
        font=("Comic Sans MS", title_font_size, "bold"),
        pady=title_pady,
    )

    top_pady = max(int(20 * game_info.app.get_window_scale()), 10)
    bottom_pady = max(int(10 * game_info.app.get_window_scale()), 5)
    label.pack(pady=(top_pady, bottom_pady))

    turn_font_size = game_info.get_responsive_font_size(22)
    turn_pady = max(int(5 * game_info.app.get_window_scale()), 3)

    game_info.turn_label = tk.Label(
        parent_frame,
        text="",
        fg="#FF69B4",
        bg="#87CEEB",
        font=("Comic Sans MS", turn_font_size, "bold"),
        pady=turn_pady,
    )

    turn_top_pady = max(int(10 * game_info.app.get_window_scale()), 5)
    turn_bottom_pady = max(int(20 * game_info.app.get_window_scale()), 10)
    game_info.turn_label.pack(pady=(turn_top_pady, turn_bottom_pady))

    game_info.update_turn_label()
