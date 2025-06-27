import tkinter as tk


def menu_button(app):
    menu_btn = tk.Button(
        app.content_frame,
        text="🏠 Return to menu 🏠",
        fg="white",
        bg="#FF6347",
        font=("Comic Sans MS", 18, "bold"),
        padx=25,
        pady=15,
        relief="raised",
        bd=5,
        activebackground="#DC143C",
        activeforeground="white",
        cursor="hand2",
        command=lambda: app.set_game_state(0, 0),
    )

    def on_enter_menu(e):
        menu_btn.config(
            bg="#DC143C", relief="sunken", font=("Comic Sans MS", 20, "bold")
        )

    def on_leave_menu(e):
        menu_btn.config(
            bg="#FF6347", relief="raised", font=("Comic Sans MS", 18, "bold")
        )

    menu_btn.bind("<Enter>", on_enter_menu)
    menu_btn.bind("<Leave>", on_leave_menu)
    menu_btn.pack(side="bottom", pady=20)
