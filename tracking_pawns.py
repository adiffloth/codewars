from cw_test import test


def pawn_move_tracker(moves):

    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]

    # pp = pprint.PrettyPrinter()
    # pp.pprint(board)
    # print()

    for i in range(len(moves)):

        b_turn = i % 2  # Who's turn is it?
        x_tgt, y_tgt = ord(moves[i][-2]) - 97, 8 - int(moves[i][-1])  # Set target x,y coords
        # Set source x, depends on whether this is a take or not
        x_src = (ord(moves[i][0]) - 97) if moves[i][1] == 'x' else x_tgt

        # Set turn-based variables
        if b_turn:
            skip_row = [3, 1, 2]
            my_marker = 'p'
            opp_marker = 'P'
            direction = -1
        else:
            skip_row = [4, 5, 6]
            my_marker = 'P'
            opp_marker = 'p'
            direction = 1

        # Set source y coord
        y_src = 0
        if y_tgt == skip_row[0]:  # Possible first pawn move
            for j in skip_row[1:]:
                if board[j][x_src] == my_marker:
                    y_src = j
        else:  # All other moves, only one possible source row
            y_src = y_tgt + direction

        # Check for valid moves
        if (board[y_src][x_src] == my_marker) and ((board[y_tgt][x_tgt] == '.' and moves[i][1] != 'x') or (board[y_tgt][x_tgt] == opp_marker and moves[i][1] == 'x')):
            valid = True
        else:
            valid = False

        if valid:  # Update board
            board[y_tgt][x_tgt] = 'p' if b_turn else 'P'
            board[y_src][x_src] = '.'
        else:
            return moves[i] + ' is invalid'

        # pp.pprint(board)
        # print()

    return board


##############


if __name__ == "__main__":

    # import pprint
    # pp = pprint.PrettyPrinter()
    # pp.pprint(pawn_move_tracker(['c3','c6']))

    test.assert_equals(pawn_move_tracker(['a4', 'a5', 'b4', 'b5', 'c4', 'b4']), 'b4 is invalid')

    test.assert_equals(pawn_move_tracker(['e4', 'd5', 'dxe4']), 'dxe4 is invalid')

    test.assert_equals(pawn_move_tracker(["c3"]), [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "P", ".", ".", ".", ".", "."],
        ["P", "P", ".", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]])

    test.assert_equals(pawn_move_tracker(["c3", 'c6']), [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", ".", "p", "p", "p", "p", "p"],
        [".", ".", "p", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "P", ".", ".", ".", ".", "."],
        ["P", "P", ".", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]])

    test.assert_equals(pawn_move_tracker(["d4", "d5", "f3", "c6", "f4"]), [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", ".", ".", "p", "p", "p", "p"],
        [".", ".", "p", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "P", ".", "P", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", ".", "P", ".", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]])

    test.assert_equals(pawn_move_tracker(["d4", "d5", "f3", "c6", "f4", "c5", "dxc5"]), [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", ".", ".", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", "P", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "P", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", ".", "P", ".", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]])

    test.assert_equals(pawn_move_tracker(["e3", "d6", "e4", "a6"]), [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", "p", "p", ".", "p", "p", "p", "p"],
        ["p", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", "P", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", ".", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]])

    test.assert_equals(pawn_move_tracker(["e4", "d5", "d3", "dxe4"]), [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", ".", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", "p", ".", ".", "."],
        [".", ".", ".", "P", ".", ".", ".", "."],
        ["P", "P", "P", ".", ".", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]])
