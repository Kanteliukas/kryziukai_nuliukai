from game_types import (
    select_game_type,
    play_single_player,
    play_multiplayer,
    play_computers,
    get_players_values,
)
from print_board import print_board

BOARD = {
    0: ["A", "B", "C"],
    1: ["-", "-", "-"],
    2: ["-", "-", "-"],
    3: ["-", "-", "-"],
}


def play_tic_tac_toe() -> str:
    """This function is the main function for playing tic tac toe game."""

    board = BOARD
    game_types = {
        1: play_single_player,
        2: play_multiplayer,
        3: play_computers,
    }
    option = select_game_type()

    print_board(board)
    player_1, player_2 = get_players_values()

    if option in game_types:
        for game_type, game_to_play in game_types.items():
            if option == game_type:
                result = game_to_play(player_1, player_2, board)
    else:
        return "bye bye"

    if result == True:
        print("You won")
    else:
        print("It's a tie")


play_tic_tac_toe()
