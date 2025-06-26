def check_row(game_info):
    x = 0
    for i in range(3):
        if game_info.map[x] == game_info.map[x + 1] == game_info.map[
            x + 2
        ] and game_info.map[x] in [1, 2]:
            if game_info.map[x] == 1:
                print("Player 1 victory")
            else:
                print("Player 2 victory")
            return game_info.map[x]
        x += 3
    return 0


def check_col(game_info):
    x = 0
    for i in range(3):
        if game_info.map[x] == game_info.map[x + 3] == game_info.map[
            x + 6
        ] and game_info.map[x] in [1, 2]:
            if game_info.map[x] == 1:
                print("Player 1 victory")
            else:
                print("Player 2 victory")
            return game_info.map[x]
        x += 1
    return 0


def check_diagonal(game_info):
    if game_info.map[0] == game_info.map[4] == game_info.map[8] and game_info.map[
        0
    ] in [1, 2]:
        if game_info.map[0] == 1:
            print("Player 1 victory")
        else:
            print("Player 2 victory")
        return game_info.map[0]

    if game_info.map[2] == game_info.map[4] == game_info.map[6] and game_info.map[
        2
    ] in [1, 2]:
        if game_info.map[2] == 1:
            print("Player 1 victory")
        else:
            print("Player 2 victory")
        return game_info.map[2]

    return 0


def game_check(game_info):
    winner = check_row(game_info) or check_col(game_info) or check_diagonal(game_info)
    return winner


def events_hooks(canvas, game_info):
    game_info.hover_image_id = None

    def on_click(event):
        if game_info.hover_image_id is not None:
            canvas.delete(game_info.hover_image_id)
            game_info.hover_image_id = None

        for i, (x1, y1, x2, y2) in enumerate(game_info.rect_coords):
            if x1 <= event.x <= x2 and y1 <= event.y <= y2:
                if game_info.map[i] == 0:
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2
                    if game_info.player_turn == 0:
                        img_id = canvas.create_image(cx, cy, image=game_info.player1)
                        game_info.image_ids[i] = img_id
                        game_info.update_map(i, game_info.player_turn)
                        game_info.player_turn = 1
                    else:
                        img_id = canvas.create_image(cx, cy, image=game_info.player2)
                        game_info.image_ids[i] = img_id
                        game_info.update_map(i, game_info.player_turn)
                        game_info.player_turn = 0
                    if winner := game_check(game_info):
                        print(f"Winner is {winner}")
                    game_info.update_turn_label()
                break

    def on_motion(event):

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
