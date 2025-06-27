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
                text="👥 Player vs Player",
                font=("Comic Sans MS", 18, "bold"),
                bg="#FFB6C1",
                fg="#FF1493",
                padx=20,
                pady=15,
                relief="raised",
                bd=5,
                activebackground="#FF69B4",
                activeforeground="white",
                cursor="hand2",
                command=lambda: app.set_game_state(1, 0),
            )

            app.mode_buttons["pvia"] = tk.Button(
                app.content_frame,
                text="🤖 Player vs IA",
                font=("Comic Sans MS", 18, "bold"),
                bg="#98FB98",
                fg="#228B22",
                padx=20,
                pady=15,
                relief="raised",
                bd=5,
                activebackground="#32CD32",
                activeforeground="white",
                cursor="hand2",
                command=lambda: app.set_game_state(1, 1),
            )

            def on_enter_pvp(e):
                app.mode_buttons["pvp"].config(
                    bg="#FF69B4", fg="white", relief="sunken"
                )

            def on_leave_pvp(e):
                app.mode_buttons["pvp"].config(
                    bg="#FFB6C1", fg="#FF1493", relief="raised"
                )

            def on_enter_pvia(e):
                app.mode_buttons["pvia"].config(
                    bg="#32CD32", fg="white", relief="sunken"
                )

            def on_leave_pvia(e):
                app.mode_buttons["pvia"].config(
                    bg="#98FB98", fg="#228B22", relief="raised"
                )

            app.mode_buttons["pvp"].bind("<Enter>", on_enter_pvp)
            app.mode_buttons["pvp"].bind("<Leave>", on_leave_pvp)
            app.mode_buttons["pvia"].bind("<Enter>", on_enter_pvia)
            app.mode_buttons["pvia"].bind("<Leave>", on_leave_pvia)

        app.mode_buttons["pvp"].pack(pady=10)
        app.mode_buttons["pvia"].pack(pady=10)
        app.buttons_visible = True


def build_homepage(app):
    app.buttons_visible = False
    app.mode_buttons.clear()

    app.content_frame = tk.Frame(app.window, bg="#87CEEB")
    app.content_frame.pack(expand=True, fill="both")

    title_label = tk.Label(
        app.content_frame,
        text="🧋 Tic Tac Toe Boba 🧋",
        font=("Comic Sans MS", 32, "bold"),
        bg="#87CEEB",
        fg="#4169E1",
        pady=20,
    )
    title_label.pack(pady=(60, 30))

    play_button = tk.Button(
        app.content_frame,
        text="🎮 Play Tic Tac Toe! 🎮",
        font=("Comic Sans MS", 20, "bold"),
        bg="#FFD700",
        fg="#FF4500",
        padx=30,
        pady=20,
        relief="raised",
        bd=6,
        activebackground="#FFA500",
        activeforeground="white",
        cursor="hand2",
        command=lambda: button_play_click(app),
    )

    def on_enter_play(e):
        play_button.config(
            bg="#FFA500",
            fg="white",
            relief="sunken",
            font=("Comic Sans MS", 22, "bold"),
        )

    def on_leave_play(e):
        play_button.config(
            bg="#FFD700",
            fg="#FF4500",
            relief="raised",
            font=("Comic Sans MS", 20, "bold"),
        )

    play_button.bind("<Enter>", on_enter_play)
    play_button.bind("<Leave>", on_leave_play)
    play_button.pack(pady=(0, 20))

    return app.content_frame
