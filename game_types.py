import random
from typing import List, Any, Dict, Set, Tuple, Optional, Union
from check_if_won import check_if_won
from kryziukai_nuliukai import BOARD
from print_board import print_board
from make_moves import make_move


def get_players_values() -> Tuple[str]:
    """Function selects which player will have X and O values."""

    values = ["O", "X"]
    player_1_value = random.choice(values)
    values.remove(player_1_value)
    player_2_value = values[0]
    print(
        f"""Player 1 value is: {player_1_value}
Player 2 value is: {player_2_value}"""
    )
    return player_1_value, player_2_value


def select_game_type() -> int:
    """Function asks player to choose game type from 3 possible options:
    1. Single player;
    2. Multiplayer;
    3. AI plays."""

    game_type_string = """Select game type, enter option number:
    1. Single player
    2. Multiplayer
    3. AI plays
    """
    user_input = input(game_type_string)
    try:
        user_input = int(user_input)
    except ValueError as e:
        raise e
    return user_input

def play_single_player(player_1_value: str, player_2_value: str, board: dict) -> bool:
    """Function is written for single player game type logic.
    Checks which player has value 'X' and gives them the priority to start the game.
    Calls function make_move for player to select the cell.
    Checks if player has won.
    Returns the overall result in boolean form whether the player has won or it is a tie."""

    taken_values = []
    has_won = False
    counter = 1
    while True:
        if player_1_value == "X":
            board, has_won, taken_values = make_move(
                board, player_1_value, "human", taken_values
            )
            if has_won == True:
                return True
            counter += 1

            if counter > 9:
                return False

        board, has_won, taken_values = make_move(
            board, player_2_value, "computer", taken_values
        )
        if has_won == True:
            return True
        counter += 1

        if player_1_value == "O":
            if counter > 9:
                return False

            board, has_won, taken_values = make_move(
                board, player_1_value, "human", taken_values
            )
            if has_won == True:
                return True
            counter += 1


def play_multiplayer(player_1_value: str, player_2_value: str, board: dict) -> bool:
    """Function is written for multiplayer game type logic.
    Checks which player has value 'X' and gives them the priority to start the game.
    Calls function make_move for player to select the cell.
    Checks if player has won.
    Returns the overall result in boolean form whether the player has won or it is a tie."""

    has_won = False
    counter = 1
    while True:
        if player_1_value == "X":
            board, has_won, _ = make_move(
                board, player_1_value, "human", taken_values=[]
            )
            if has_won == True:
                return True
            counter += 1

            if counter > 9:
                return False

        board, has_won, _ = make_move(board, player_2_value, "human", taken_values=[])
        if has_won == True:
            return True
        counter += 1

        if player_1_value == "O":
            if counter > 9:
                return False

            board, has_won, _ = make_move(
                board, player_1_value, "human", taken_values=[]
            )
            if has_won == True:
                return True
            counter += 1


def play_computers(player_1_value: str, player_2_value: str, board: dict) -> bool:
    """Function is written for AI plays game type logic.
    Checks which player has value 'X' and gives them the priority to start the game.
    Calls function make_move for player to select the cell.
    Checks if player has won.
    Returns the overall result in boolean form whether the player has won or it is a tie."""

    taken_values = []
    has_won = False
    counter = 1
    while True:
        if counter > 9:
            return False
        if player_1_value == "X":
            board, has_won, taken_values = make_move(
                board, player_1_value, "computer", taken_values
            )
            if has_won == True:
                return True
            counter += 1

            if counter > 9:
                return False

        board, has_won, taken_values = make_move(
            board, player_2_value, "computer", taken_values
        )
        if has_won == True:
            return True
        counter += 1

        if player_1_value == "O":
            if counter > 9:
                return False

            board, has_won, taken_values = make_move(
                board, player_1_value, "computer", taken_values
            )
            if has_won == True:
                return True
            counter += 1
