import tkinter as tk


def button_play_click(app):
    if app.buttons_visible:
        for btn in app.mode_buttons.values():
            btn.pack_forget()
        app.buttons_visible = False
    else:
        if not app.mode_buttons:
            app.mode_buttons["pvp"] = tk.Button(
                app.content_frame,
                text="Player vs Player",
                font=("Arial", 16),
                padx=10,
                pady=5,
                command=lambda: app.set_game_state(1),
            )
            app.mode_buttons["pvia"] = tk.Button(
                app.content_frame,
                text="Player vs IA",
                font=("Arial", 16),
                padx=10,
                pady=5,
                command=lambda: app.set_game_state(1),
            )
        app.mode_buttons["pvp"].pack(pady=5)
        app.mode_buttons["pvia"].pack(pady=5)
        app.buttons_visible = True


def build_homepage(app):
    app.buttons_visible = False
    app.mode_buttons.clear()

    app.content_frame = tk.Frame(app.window, bg="grey")
    app.content_frame.pack(expand=True, fill="both")

    title_label = tk.Label(
        app.content_frame,
        text="Tic Tac Toe Boba",
        font=("Arial", 24, "bold"),
        bg="grey",
        fg="white",
    )
    title_label.pack(pady=(60, 20))

    play_button = tk.Button(
        app.content_frame,
        text="Play Tic Tac Toe",
        font=("Arial", 16),
        padx=20,
        pady=10,
        command=lambda: button_play_click(app),
    )
    play_button.pack(pady=(0, 5))

    return app.content_frame
