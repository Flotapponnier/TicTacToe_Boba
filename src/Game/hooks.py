import tkinter as tk
import random


def check_row(game_info):
    x = 0
    for i in range(3):
        if game_info.map[x] == game_info.map[x + 1] == game_info.map[
            x + 2
        ] and game_info.map[x] in [1, 2]:
            return game_info.map[x]
        x += 3
    return 0


def check_col(game_info):
    x = 0
    for i in range(3):
        if game_info.map[x] == game_info.map[x + 3] == game_info.map[
            x + 6
        ] and game_info.map[x] in [1, 2]:
            return game_info.map[x]
        x += 1
    return 0


def check_diagonal(game_info):
    if game_info.map[0] == game_info.map[4] == game_info.map[8] and game_info.map[
        0
    ] in [1, 2]:
        return game_info.map[0]

    if game_info.map[2] == game_info.map[4] == game_info.map[6] and game_info.map[
        2
    ] in [1, 2]:
        return game_info.map[2]

    return 0


def is_board_full(game_info):
    return all(cell != 0 for cell in game_info.map)


def game_check(game_info):
    winner = check_row(game_info) or check_col(game_info) or check_diagonal(game_info)
    if winner:
        return winner
    elif is_board_full(game_info):
        return "tie"
    return 0


def show_victory(game_info, winner, app):
    if winner == "tie":
        winner_text = "🤝 It's a Tie! 🤝"
        winner_color = "#800080"
    elif app.type_game == 1:
        if winner == 1:
            winner_text = "🎉 Black Boba (AI) Wins! 🎉"
            winner_color = "#4B0082"
        else:
            winner_text = "🎉 Boba (You) Wins! 🎉"
            winner_color = "#FF69B4"
    else:
        if winner == 1:
            winner_text = "🎉 Black Boba Wins! 🎉"
            winner_color = "#4B0082"
        else:
            winner_text = "🎉 Boba Wins! 🎉"
            winner_color = "#FF69B4"

    game_info.turn_label.config(text=winner_text, fg=winner_color)

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
        command=lambda: restart_game(app),
    )

    def on_enter_again(e):
        play_again_btn.config(
            bg="#228B22", relief="sunken", font=("Comic Sans MS", 22, "bold")
        )

    def on_leave_again(e):
        play_again_btn.config(
            bg="#32CD32", relief="raised", font=("Comic Sans MS", 20, "bold")
        )

    play_again_btn.bind("<Enter>", on_enter_again)
    play_again_btn.bind("<Leave>", on_leave_again)
    play_again_btn.pack(pady=15)
    game_info.play_again_button = play_again_btn


def restart_game(app):
    app.set_game_state(1, app.type_game)


def get_available_moves(game_info):
    return [i for i in range(9) if game_info.map[i] == 0]


def ai_make_move(canvas, game_info, app):
    if game_info.game_ended:
        return

    available_moves = get_available_moves(game_info)
    if not available_moves:
        return

    ai_choice = random.choice(available_moves)

    x1, y1, x2, y2 = game_info.rect_coords[ai_choice]
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    img_id = canvas.create_image(cx, cy, image=game_info.player2)
    game_info.image_ids[ai_choice] = img_id
    game_info.update_map(ai_choice, 1)
    game_info.player_turn = 0

    result = game_check(game_info)
    if result:
        game_info.game_ended = True
        show_victory(game_info, result, app)
    else:
        game_info.update_turn_label()


def events_hooks(canvas, game_info, app):
    game_info.hover_image_id = None
    game_info.game_ended = False

    def on_click(event):
        if game_info.game_ended:
            return

        if game_info.hover_image_id is not None:
            canvas.delete(game_info.hover_image_id)
            game_info.hover_image_id = None

        for i, (x1, y1, x2, y2) in enumerate(game_info.rect_coords):
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                if game_info.map[i] == 0:
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2

                    if app.type_game == 0:
                        if game_info.player_turn == 0:
                            img_id = canvas.create_image(
                                cx, cy, image=game_info.player1
                            )
                            game_info.image_ids[i] = img_id
                            game_info.update_map(i, game_info.player_turn)
                            game_info.player_turn = 1
                        else:
                            img_id = canvas.create_image(
                                cx, cy, image=game_info.player2
                            )
                            game_info.image_ids[i] = img_id
                            game_info.update_map(i, game_info.player_turn)
                            game_info.player_turn = 0

                        result = game_check(game_info)
                        if result:
                            game_info.game_ended = True
                            show_victory(game_info, result, app)
                        else:
                            game_info.update_turn_label()

                    elif app.type_game == 1:
                        if game_info.player_turn == 0:
                            img_id = canvas.create_image(
                                cx, cy, image=game_info.player1
                            )
                            game_info.image_ids[i] = img_id
                            game_info.update_map(i, 0)
                            game_info.player_turn = 1

                            result = game_check(game_info)
                            if result:
                                game_info.game_ended = True
                                show_victory(game_info, result, app)
                            else:
                                game_info.update_turn_label()
                                canvas.after(
                                    500, lambda: ai_make_move(canvas, game_info, app)
                                )
                        else:
                            return
                break

    def on_motion(event):
        if game_info.game_ended:
            return

        if app.type_game == 1 and game_info.player_turn == 1:
            return

        hovered_index = None
        for i, (x1, y1, x2, y2) in enumerate(game_info.rect_coords):
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                hovered_index = i
                break

        if game_info.hover_image_id is not None:
            canvas.delete(game_info.hover_image_id)
            game_info.hover_image_id = None

        if hovered_index is not None and game_info.map[hovered_index] == 0:
            x1, y1, x2, y2 = game_info.rect_coords[hovered_index]
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            if game_info.player_turn == 0:
                hover_image = game_info.player1_transparent
            else:
                hover_image = game_info.player2_transparent
            game_info.hover_image_id = canvas.create_image(cx, cy, image=hover_image)

    def on_leave(event):
        if game_info.hover_image_id is not None:
            canvas.delete(game_info.hover_image_id)
            game_info.hover_image_id = None

    canvas.bind("<Button-1>", on_click)
    canvas.bind("<Motion>", on_motion)
    canvas.bind("<Leave>", on_leave)
