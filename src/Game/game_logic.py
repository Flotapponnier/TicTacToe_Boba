def check_winning_row(game_map):
    x = 0
    for i in range(3):
        if game_map[x] == game_map[x + 1] == game_map[x + 2] and game_map[x] in [1, 2]:
            return game_map[x]
        x += 3
    return 0


def check_winning_column(game_map):
    x = 0
    for i in range(3):
        if game_map[x] == game_map[x + 3] == game_map[x + 6] and game_map[x] in [1, 2]:
            return game_map[x]
        x += 1
    return 0


def check_winning_diagonal(game_map):
    if game_map[0] == game_map[4] == game_map[8] and game_map[0] in [1, 2]:
        return game_map[0]
    if game_map[2] == game_map[4] == game_map[6] and game_map[2] in [1, 2]:
        return game_map[2]
    return 0


def is_board_full(game_map):
    return all(cell != 0 for cell in game_map)


def check_game_state(game_info):
    winner = (
        check_winning_row(game_info.map)
        or check_winning_column(game_info.map)
        or check_winning_diagonal(game_info.map)
    )
    if winner:
        return winner
    elif is_board_full(game_info.map):
        return "tie"
    return 0


def get_empty_positions(game_map):
    return [i for i in range(9) if game_map[i] == 0]
