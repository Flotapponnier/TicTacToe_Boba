import tkinter as tk


def display_game_result(game_info, result, app):
    message_text, message_color = get_result_message(result, app)
    game_info.turn_label.config(text=message_text, fg=message_color)
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
    play_again_btn = tk.Button(
        game_info.turn_label.master,
        text="🔄 Play Again! 🔄",
        fg="white",
        bg="#32CD32",
        font=("Comic Sans MS", 20, "bold"),
        padx=25,
        pady=15,
        relief="raised",
        bd=5,
        activebackground="#228B22",
        activeforeground="white",
        cursor="hand2",
        command=lambda: restart_current_game(app),
    )

    def on_button_hover_enter(e):
        play_again_btn.config(
            bg="#228B22", relief="sunken", font=("Comic Sans MS", 22, "bold")
        )

    def on_button_hover_leave(e):
        play_again_btn.config(
            bg="#32CD32", relief="raised", font=("Comic Sans MS", 20, "bold")
        )

    play_again_btn.bind("<Enter>", on_button_hover_enter)
    play_again_btn.bind("<Leave>", on_button_hover_leave)
    play_again_btn.pack(pady=15)
    game_info.play_again_button = play_again_btn


def restart_current_game(app):
    app.set_game_state(1, app.type_game)
