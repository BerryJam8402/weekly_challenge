def validate_tictactoe(board):
    # Count X's and O's
    x_count = 0
    o_count = 0

    for row in board:
        for marking_square in row:
            if marking_square == "X":
                x_count = x_count + 1
            elif marking_square == "O":
                o_count = o_count + 1

    # TODO 1: Check that X went first
    # O can never have more moves than X
    if o_count > x_count:
        return False

    # TODO 2: Check alternating turns
    # X can only be ahead by exactly 1, or tied with O
    if x_count - o_count > 1:
        return False

    # TODO 3: Check win states

    # Helper function to check if a given player has won
    def has_won(player):
        # Check rows
        row_num = 0

        while row_num < 3:
            if board[row_num][0] == player and board[row_num][1] == player and board[row_num][2] == player:
                return True
            row_num = row_num + 1

        # Check columns
        col_num = 0
        while col_num < 3:
            if board[0][col_num] == player and board[1][col_num] == player and board[2][col_num] == player:
                return True
            col_num = col_num + 1

        # Check diagonal top-left to bottom-right
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True

        # Check diagonal top-right to bottom-left
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True

        # No winning line found
        return False

    x_won = has_won("X")
    o_won = has_won("O")

    # Both players can't win — game stops at the first win
    if x_won is True and o_won is True:
        return False

    # If X won, X must have gone last, so X count should be 1 more than O
    if x_won is True:
        if x_count != o_count + 1:
            return False

    # If O won, O must have gone last, so counts should be equal
    if o_won is True:
        if x_count != o_count:
            return False

    return True


# Tests

print(validate_tictactoe(["X  ", "   ", "   "]))
# output = true
# X always goes first, so one X is valid.

print(validate_tictactoe(["O  ", "   ", "   "]))
# output = false
# O cannot make the first move.

print(validate_tictactoe(["X X", " O ", "   "]))
# output = true
# X played twice, O once.
# This follows alternating turns = valid.

print(validate_tictactoe(["XOX", " X ", "   "]))
# output = false
# X has 3 moves while O has 1.
# Players must alternate, so move counts are invalid.

print(validate_tictactoe(["XXX", "OO ", "   "]))
# output = true
# X has 3 moves, O has 2.
# X completes a row on its turn, so the game can end here.

print(validate_tictactoe(["XXX", "   ", "OOO"]))
# output = false
# Both players cannot win in the same valid game.
# The game would stop as soon as the first win happens.
