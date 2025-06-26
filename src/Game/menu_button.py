import tkinter as tk


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
