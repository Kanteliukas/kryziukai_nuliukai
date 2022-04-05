import random
import time
from typing import List, Tuple
from print_board import print_board
from check_if_won import check_if_won


def convert_selection_value(selection) -> List[int]:
    """Function converts human player selection from string value to integer values
    for column number and row number on the board.
    Returns converted values."""

    result = []
    columns = ["A", "B", "C"]
    for symbol in selection:
        if symbol.upper() in columns:
            symbol = columns.index(symbol.upper())
        elif symbol.isnumeric():
            symbol = int(symbol)
        result.append(symbol)
    return result


def add_value_for_selection(
    board: dict, selection: str, value: str
) -> Tuple[dict, tuple]:
    """Function adds value ('X' or 'O') to human player selected cell.
    Returns updated board and human selection in tuple form."""

    while True:
        try:
            column, row = convert_selection_value(selection)
        except ValueError as e:
            print("Wrong format")
            selection = player_makes_move()
            continue

        if board[row][column] == "-":
            board[row][column] = value
            selection = (row, column)
            print_board(board)
            return board, selection
        else:
            print("Cell is taken")
            print_board(board)
            selection = player_makes_move()
            continue


def player_makes_move() -> str:
    """Function asks user to make a selection on a board.
    Returns user input."""

    selection_string = """Type column name, row name and value to put in the board,
format to use: B2
    """
    user_input = input(selection_string)
    return user_input


def computer_makes_move(
    value: str, board: dict, taken: list = []
) -> Tuple[dict, tuple]:
    """Function selects cell for a computer in a random choice pattern and
    removes selection from (available) options list.
    Then checks if the cell is already occupied.
    If cell is not occupied, function updates the board with
    the computer value for selected cell.
    If cell is occupied, function loops again until computer chooses unoccupied cell.
    Returns updated board and computer selection in tuple form."""

    options = [
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
        (3, 0),
        (3, 1),
        (3, 2),
    ]
    selection = ""
    while selection == "" or selection in taken:
        selection = random.choice(options)
        options.remove(selection)
    else:
        board[selection[0]][selection[1]] = value
        time.sleep(0.5)
        print_board(board)
        return board, selection


def make_move(
    board: dict, value: str, player: str, taken_values: list
) -> Tuple[dict, bool, list]:
    """Function holds logic for human player or computer player to make a move on a board.
    If player is human, function calls other functions
    for selecting or adding human player value to the board.
    If player is computer, function calls other functions
    for selecting and adding computer player value to the board.
    Function also checks if player has won.
    Returns updated board, boolean if player has won and already taken values on the board."""

    if player == "human":
        selection = player_makes_move()
        board, selection = add_value_for_selection(board, selection, value)
        taken_values.append(selection)
        has_won = check_if_won(board)
        return board, has_won, taken_values
    elif player == "computer":
        board, selection = computer_makes_move(value, board, taken=taken_values)
        taken_values.append(selection)
        has_won = check_if_won(board)
        return board, has_won, taken_values
