import tkinter as tk


def menu_button(app):
    scale = app.get_window_scale()
    font_size = max(int(18 * scale), 12)
    padx = max(int(25 * scale), 15)
    pady = max(int(15 * scale), 10)
    bottom_pady = max(int(20 * scale), 10)

    menu_btn = tk.Button(
        app.content_frame,
        text="🏠 Return to menu 🏠",
        fg="white",
        bg="#FF6347",
        font=("Comic Sans MS", font_size, "bold"),
        padx=padx,
        pady=pady,
        relief="raised",
        bd=5,
        activebackground="#DC143C",
        activeforeground="white",
        cursor="hand2",
        command=lambda: app.set_game_state(0, 0),
    )

    def on_enter_menu(e):
        hover_font_size = max(int(20 * scale), 14)
        menu_btn.config(
            bg="#DC143C",
            relief="sunken",
            font=("Comic Sans MS", hover_font_size, "bold"),
        )

    def on_leave_menu(e):
        normal_font_size = max(int(18 * scale), 12)
        menu_btn.config(
            bg="#FF6347",
            relief="raised",
            font=("Comic Sans MS", normal_font_size, "bold"),
        )

    menu_btn.bind("<Enter>", on_enter_menu)
    menu_btn.bind("<Leave>", on_leave_menu)
    menu_btn.pack(side="bottom", pady=bottom_pady)
