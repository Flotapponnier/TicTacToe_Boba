import tkinter as tk
from .game_logic import check_game_state
from .ai_player import make_ai_move
from .player_actions import handle_player_move, can_player_move


def setup_game_events(canvas, game_info, app):
    game_info.hover_image_id = None
    game_info.game_ended = False

    if app.type_game == 1 and game_info.player_turn == 1:
        canvas.after(500, lambda: make_ai_move(canvas, game_info, app))

    def on_canvas_click(event):
        if not can_player_move(game_info, app):
            return

        clear_hover_effect(canvas, game_info)

        clicked_position = find_clicked_position(event, game_info.rect_coords)
        if clicked_position is not None and game_info.map[clicked_position] == 0:
            handle_player_move(canvas, game_info, app, clicked_position)

    def on_mouse_motion(event):
        if not should_show_hover(game_info, app):
            return

        clear_hover_effect(canvas, game_info)

        hovered_position = find_clicked_position(event, game_info.rect_coords)
        if hovered_position is not None and game_info.map[hovered_position] == 0:
            show_hover_effect(canvas, game_info, hovered_position)

    def on_mouse_leave(event):
        clear_hover_effect(canvas, game_info)

    canvas.bind("<Button-1>", on_canvas_click)
    canvas.bind("<Motion>", on_mouse_motion)
    canvas.bind("<Leave>", on_mouse_leave)


def find_clicked_position(event, rect_coords):
    for i, (x1, y1, x2, y2) in enumerate(rect_coords):
        if x1 <= event.x <= x2 and y1 <= event.y <= y2:
            return i
    return None


def clear_hover_effect(canvas, game_info):
    if game_info.hover_image_id is not None:
        canvas.delete(game_info.hover_image_id)
        game_info.hover_image_id = None


def show_hover_effect(canvas, game_info, position):
    x1, y1, x2, y2 = game_info.rect_coords[position]
    center_x = (x1 + x2) // 2
    center_y = (y1 + y2) // 2

    hover_image = (
        game_info.player1_transparent
        if game_info.player_turn == 0
        else game_info.player2_transparent
    )
    game_info.hover_image_id = canvas.create_image(
        center_x, center_y, image=hover_image
    )


def should_show_hover(game_info, app):
    if game_info.game_ended:
        return False
    if app.type_game == 1 and game_info.player_turn == 1:
        return False
    return True
