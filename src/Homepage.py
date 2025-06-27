import tkinter as tk


def get_responsive_font_size(app, base_size):
    scale = app.get_window_scale()
    return max(int(base_size * scale), 12)


def get_responsive_padding(app, base_padding):
    """Calcule le padding responsive"""
    scale = app.get_window_scale()
    return max(int(base_padding * scale), 5)


def button_play_click(app):
    if app.buttons_visible:
        for btn in app.mode_buttons.values():
            btn.pack_forget()
        app.buttons_visible = False
    else:
        if not app.mode_buttons:
            font_size = get_responsive_font_size(app, 18)
            padx = get_responsive_padding(app, 20)
            pady = get_responsive_padding(app, 15)

            app.mode_buttons["pvp"] = tk.Button(
                app.content_frame,
                text="👥 Player vs Player",
                font=("Comic Sans MS", font_size, "bold"),
                bg="#FFB6C1",
                fg="#FF1493",
                padx=padx,
                pady=pady,
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
                font=("Comic Sans MS", font_size, "bold"),
                bg="#98FB98",
                fg="#228B22",
                padx=padx,
                pady=pady,
                relief="raised",
                bd=5,
                activebackground="#32CD32",
                activeforeground="white",
                cursor="hand2",
                command=lambda: app.set_game_state(1, 1),
            )

            def on_enter_pvp(e):
                hover_font_size = get_responsive_font_size(app, 20)
                app.mode_buttons["pvp"].config(
                    bg="#FF69B4",
                    fg="white",
                    relief="sunken",
                    font=("Comic Sans MS", hover_font_size, "bold"),
                )

            def on_leave_pvp(e):
                normal_font_size = get_responsive_font_size(app, 18)
                app.mode_buttons["pvp"].config(
                    bg="#FFB6C1",
                    fg="#FF1493",
                    relief="raised",
                    font=("Comic Sans MS", normal_font_size, "bold"),
                )

            def on_enter_pvia(e):
                hover_font_size = get_responsive_font_size(app, 20)
                app.mode_buttons["pvia"].config(
                    bg="#32CD32",
                    fg="white",
                    relief="sunken",
                    font=("Comic Sans MS", hover_font_size, "bold"),
                )

            def on_leave_pvia(e):
                normal_font_size = get_responsive_font_size(app, 18)
                app.mode_buttons["pvia"].config(
                    bg="#98FB98",
                    fg="#228B22",
                    relief="raised",
                    font=("Comic Sans MS", normal_font_size, "bold"),
                )

            app.mode_buttons["pvp"].bind("<Enter>", on_enter_pvp)
            app.mode_buttons["pvp"].bind("<Leave>", on_leave_pvp)
            app.mode_buttons["pvia"].bind("<Enter>", on_enter_pvia)
            app.mode_buttons["pvia"].bind("<Leave>", on_leave_pvia)

        padding = get_responsive_padding(app, 10)
        app.mode_buttons["pvp"].pack(pady=padding)
        app.mode_buttons["pvia"].pack(pady=padding)
        app.buttons_visible = True


def build_homepage(app):
    app.buttons_visible = False
    app.mode_buttons.clear()

    app.content_frame = tk.Frame(app.window, bg="#87CEEB")
    app.content_frame.pack(expand=True, fill="both")

    title_font_size = get_responsive_font_size(app, 32)
    title_pady = get_responsive_padding(app, 20)

    title_label = tk.Label(
        app.content_frame,
        text="🧋 Tic Tac Toe Boba 🧋",
        font=("Comic Sans MS", title_font_size, "bold"),
        bg="#87CEEB",
        fg="#4169E1",
        pady=title_pady,
    )
    title_label.pack(
        pady=(get_responsive_padding(app, 60), get_responsive_padding(app, 30))
    )

    play_font_size = get_responsive_font_size(app, 20)
    play_padx = get_responsive_padding(app, 30)
    play_pady = get_responsive_padding(app, 20)

    play_button = tk.Button(
        app.content_frame,
        text="🎮 Play Tic Tac Toe! 🎮",
        font=("Comic Sans MS", play_font_size, "bold"),
        bg="#FFD700",
        fg="#FF4500",
        padx=play_padx,
        pady=play_pady,
        relief="raised",
        bd=6,
        activebackground="#FFA500",
        activeforeground="white",
        cursor="hand2",
        command=lambda: button_play_click(app),
    )

    def on_enter_play(e):
        hover_font_size = get_responsive_font_size(app, 22)
        play_button.config(
            bg="#FFA500",
            fg="white",
            relief="sunken",
            font=("Comic Sans MS", hover_font_size, "bold"),
        )

    def on_leave_play(e):
        normal_font_size = get_responsive_font_size(app, 20)
        play_button.config(
            bg="#FFD700",
            fg="#FF4500",
            relief="raised",
            font=("Comic Sans MS", normal_font_size, "bold"),
        )

    play_button.bind("<Enter>", on_enter_play)
    play_button.bind("<Leave>", on_leave_play)
    play_button.pack(pady=(0, get_responsive_padding(app, 20)))

    return app.content_frame
