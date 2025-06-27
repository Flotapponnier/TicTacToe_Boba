from .game_logic import check_game_state
from .game_ui import display_game_result
from .ai_player import make_ai_move


def handle_player_move(canvas, game_info, app, position):
    center_x, center_y = get_cell_center(game_info.rect_coords[position])

    if app.type_game == 0:
        handle_pvp_move(canvas, game_info, app, position, center_x, center_y)
    elif app.type_game == 1:
        handle_pva_move(canvas, game_info, app, position, center_x, center_y)


def handle_pvp_move(canvas, game_info, app, position, center_x, center_y):
    if game_info.player_turn == 0:
        place_player_piece(
            canvas, game_info, position, center_x, center_y, game_info.player1, 0
        )
        game_info.player_turn = 1
    else:
        place_player_piece(
            canvas, game_info, position, center_x, center_y, game_info.player2, 1
        )
        game_info.player_turn = 0

    check_and_handle_game_end(game_info, app)


def handle_pva_move(canvas, game_info, app, position, center_x, center_y):
    if game_info.player_turn == 0:
        place_player_piece(
            canvas, game_info, position, center_x, center_y, game_info.player1, 0
        )
        game_info.player_turn = 1

        result = check_game_state(game_info)
        if result:
            game_info.game_ended = True
            display_game_result(game_info, result, app)
        else:
            game_info.update_turn_label()
            canvas.after(500, lambda: make_ai_move(canvas, game_info, app))


def place_player_piece(
    canvas, game_info, position, center_x, center_y, image, player_value
):
    image_id = canvas.create_image(center_x, center_y, image=image)
    game_info.image_ids[position] = image_id
    game_info.update_map(position, player_value)


def get_cell_center(rect_coords):
    x1, y1, x2, y2 = rect_coords
    return (x1 + x2) // 2, (y1 + y2) // 2


def check_and_handle_game_end(game_info, app):
    result = check_game_state(game_info)
    if result:
        game_info.game_ended = True
        display_game_result(game_info, result, app)
    else:
        game_info.update_turn_label()


def can_player_move(game_info, app):
    if game_info.game_ended:
        return False
    if app.type_game == 1 and game_info.player_turn == 1:
        return False
    return True
