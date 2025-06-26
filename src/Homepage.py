import tkinter as tk

toggle_state = {"buttons_visible": False}
mode_buttons = {}


def buttonplayclick(content_frame, set_game_state, window):
    if toggle_state["buttons_visible"]:
        for btn in mode_buttons.values():
            btn.pack_forget()
        toggle_state["buttons_visible"] = False
    else:
        if not mode_buttons:
            mode_buttons["pvp"] = tk.Button(
                content_frame,
                text="Player vs Player",
                font=("Arial", 16),
                padx=10,
                pady=5,
                command=lambda: set_game_state(1, window),
            )
            mode_buttons["pvia"] = tk.Button(
                content_frame,
                text="Player vs Ia",
                font=("Arial", 16),
                padx=10,
                pady=5,
                command=lambda: set_game_state(1, window),
            )
        mode_buttons["pvp"].pack(pady=5)
        mode_buttons["pvia"].pack(pady=5)
        toggle_state["buttons_visible"] = True


def homepage(window, set_game_state):
    toggle_state["buttons_visible"] = False
    mode_buttons.clear()

    content_frame = tk.Frame(window, bg="grey")
    content_frame.pack(expand=True, fill="both")

    title_label = tk.Label(
        content_frame,
        text="Tic Tac Toe Boba",
        font=("Arial", 24, "bold"),
        bg="grey",
        fg="white",
    )
    title_label.pack(pady=(60, 20))

    button = tk.Button(
        content_frame,
        text="Play Tic Tac Toe",
        font=("Arial", 16),
        padx=20,
        pady=10,
        command=lambda: buttonplayclick(content_frame, set_game_state, window),
    )
    button.pack(pady=(0, 5))

    return content_frame
