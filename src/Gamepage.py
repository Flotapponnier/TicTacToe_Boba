import tkinter as tk


def gamepage(set_game_state, window):
    global content_frame
    content_frame = tk.Frame(window, bg="black")
    content_frame.pack(expand=True, fill="both")
    label = tk.Label(
        content_frame,
        text="Game started!",
        fg="white",
        bg="black",
        font=("Arial", 24),
    )
    label.pack(pady=(60, 20))
    menu_button = tk.Button(
        content_frame,
        text="Return to menu",
        fg="white",
        bg="black",
        font=("Arial", 24),
        command=lambda: set_game_state(0, window),
    )
    menu_button.pack()
    return content_frame
