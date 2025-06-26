import tkinter as tk


def game(app):
    app.content_frame = tk.Frame(app.window, bg="black")
    app.content_frame.pack(expand=True, fill="both")

    label = tk.Label(
        app.content_frame,
        text="Game started!",
        fg="white",
        bg="black",
        font=("Arial", 24),
    )
    label.pack(pady=(60, 20))


def menu_button(app):
    menu_button = tk.Button(
        app.content_frame,
        text="Return to menu",
        fg="white",
        bg="black",
        font=("Arial", 24),
        command=lambda: app.set_game_state(0),
    )
    menu_button.pack()


def build_gamepage(app):
    game(app)
    menu_button(app)
    return app.content_frame
