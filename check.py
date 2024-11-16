import functions

def checks(board, current_cell):
    moves = []

    #search for king position
    king = -1
    for index,aa in enumerate(board):
        if aa != "empty":
            if aa.team == board[current_cell].team:
                if aa.name == "king":
                    king = index

    # save the attributes of the classes before they are affected
    # by the piece movement

    current_piece = board[current_cell]
    not_moved = current_piece.not_moved
    if current_piece.name == "pawn":
        enpassant = current_piece.enpassant
        enpassant_direction = current_piece.enpassant_direction


    # add all posible moves after doing them
    # only add them if the king is not in check
    for ab in board[current_cell].movement(current_cell,board):
        temp = True
        temporal_board = functions.piece_movement(current_cell,ab,board[:])
        enemy_moves = functions.all_moves(board[current_cell].team,temporal_board)
        if board[current_cell].name != "king":
            for move,_ in enemy_moves:
                if move == king:
                    temp = False
            if temp:
                moves.append(ab)
        else:
            for move,_ in enemy_moves:
                king = ab[0]
                if move == king:
                    temp = False
            if temp:
                moves.append(ab)
        
        current_piece.not_moved = not_moved
        if current_piece.name == "pawn":
            current_piece.enpassant = enpassant
            current_piece.enpassant_direction = enpassant_direction

    return moves

# Takes the board and turn to see if the game ended or not
# it returns:
# 0 = ongoing
# 1 = winner
# 2 = tie
def checkmate(board, turno):
    turno = functions.change_turn(turno)
    if len(functions.all_moves_check(turno,board)) == 0:
        return 1
    else:
        # check if it is a tie
        amount_of_pieces = 0
        for aa in board:
            if aa != "empty":
                amount_of_pieces += 1
        if amount_of_pieces == 2:
            return 2
        else:
            return 0


