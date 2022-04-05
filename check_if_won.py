WIN_POSSIBILITIES = [
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(3, 0), (3, 1), (3, 2)],
    [(1, 0), (2, 0), (3, 0)],
    [(1, 1), (2, 1), (3, 1)],
    [(1, 2), (2, 2), (3, 2)],
    [(1, 0), (2, 1), (3, 2)],
    [(1, 2), (2, 1), (3, 0)],
]


def check_if_won(board: dict) -> bool:
    """Function checks if player won the game."""

    for posibility in WIN_POSSIBILITIES:
        value_1, value_2, value_3 = posibility
        row_1, column_1 = value_1
        row_2, column_2 = value_2
        row_3, column_3 = value_3
        result = (
            f"{board[row_1][column_1]}{board[row_2][column_2]}{board[row_3][column_3]}"
        )
        if result == "XXX" or result == "OOO":
            return True
        else:
            continue
    return False
