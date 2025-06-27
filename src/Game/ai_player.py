import random
from .game_logic import get_empty_positions, check_game_state
from .game_ui import display_game_result


def make_ai_move(canvas, game_info, app):
    if game_info.game_ended:
        return

    available_positions = get_empty_positions(game_info.map)
    if not available_positions:
        return

    ai_choice = select_ai_position(available_positions)
    place_ai_piece(canvas, game_info, ai_choice)

    result = check_game_state(game_info)
    if result:
        game_info.game_ended = True
        display_game_result(game_info, result, app)
    else:
        game_info.update_turn_label()


def select_ai_position(available_positions):
    return random.choice(available_positions)


def place_ai_piece(canvas, game_info, position):
    x1, y1, x2, y2 = game_info.rect_coords[position]
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    image_id = canvas.create_image(center_x, center_y, image=game_info.player2)
    game_info.image_ids[position] = image_id
    game_info.update_map(position, 1)
    game_info.player_turn = 0
