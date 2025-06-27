import tkinter as tk


def display_game_result(game_info, result, app):
    message_text, message_color = get_result_message(result, app)
    font_size = game_info.get_responsive_font_size(22)
    game_info.turn_label.config(
        text=message_text, fg=message_color, font=("Comic Sans MS", font_size, "bold")
    )
    create_play_again_button(game_info, app)


def get_result_message(result, app):
    if result == "tie":
        return "🤝 It's a Tie! 🤝", "#800080"
    elif app.type_game == 1:
        if result == 1:
            return "🎉 Black Boba (AI) Wins! 🎉", "#4B0082"
        else:
            return "🎉 Boba (You) Wins! 🎉", "#FF69B4"
    else:
        if result == 1:
            return "🎉 Black Boba Wins! 🎉", "#4B0082"
        else:
            return "🎉 Boba Wins! 🎉", "#FF69B4"


def create_play_again_button(game_info, app):
    scale = app.get_window_scale()
    font_size = max(int(20 * scale), 14)
    padx = max(int(25 * scale), 15)
    pady = max(int(15 * scale), 10)
    button_pady = max(int(15 * scale), 8)

    play_again_btn = tk.Button(
        game_info.turn_label.master,
        text="🔄 Play Again! 🔄",
        fg="white",
        bg="#32CD32",
        font=("Comic Sans MS", font_size, "bold"),
        padx=padx,
        pady=pady,
        relief="raised",
        bd=5,
        activebackground="#228B22",
        activeforeground="white",
        cursor="hand2",
        command=lambda: restart_current_game(app),
    )

    def on_button_hover_enter(e):
        hover_font_size = max(int(22 * scale), 16)
        play_again_btn.config(
            bg="#228B22",
            relief="sunken",
            font=("Comic Sans MS", hover_font_size, "bold"),
        )

    def on_button_hover_leave(e):
        normal_font_size = max(int(20 * scale), 14)
        play_again_btn.config(
            bg="#32CD32",
            relief="raised",
            font=("Comic Sans MS", normal_font_size, "bold"),
        )

    play_again_btn.bind("<Enter>", on_button_hover_enter)
    play_again_btn.bind("<Leave>", on_button_hover_leave)
    play_again_btn.pack(pady=button_pady)
    game_info.play_again_button = play_again_btn


def restart_current_game(app):
    app.set_game_state(1, app.type_game)
