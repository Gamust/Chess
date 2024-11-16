import Pieces
import random
import pygame
import configuration


# Gets the positions from a Fen string.
def get_position(position):
    rows = position.split("/")
    printing_position = []
    
    for aa in rows:
        for ab in aa:
            if ab.isdigit():
                for _ in range(int(ab)):
                    printing_position.append("empty")
            elif ab == "p":
                bpawn = Pieces.Pawn(0)
                printing_position.append(bpawn)
            elif ab == "P":
                wpawn = Pieces.Pawn(1)
                printing_position.append(wpawn)
            elif ab == "n":
                bknight = Pieces.Knight(0)
                printing_position.append(bknight)
            elif ab == "N":
                wknight =Pieces.Knight(1)
                printing_position.append(wknight)
            elif ab == "r":
                brook = Pieces.Rook(0)
                printing_position.append(brook)
            elif ab == "R":
                wrook = Pieces.Rook(1)
                printing_position.append(wrook)
            elif ab == "b":
                bbishop = Pieces.Bishop(0)
                printing_position.append(bbishop)
            elif ab == "B":
                wbishop = Pieces.Bishop(1)
                printing_position.append(wbishop)
            elif ab == "k":
                bking = Pieces.King(0)
                printing_position.append(bking)
            elif ab == "K":
                wking = Pieces.King(1)
                printing_position.append(wking)
            elif ab == "q":
                bqueen = Pieces.Queen(0)
                printing_position.append(bqueen)
            elif ab == "Q":
                wqueen = Pieces.Queen(1)
                printing_position.append(wqueen)

    return printing_position


# After inputing a Fen string it gives back all the components to be read by other functions
# the return is: 
# - position of pieces
# - which team turn it is
# - posibility to castle
# - if there is any enpassant
def Fen(Fen_string):
    field = Fen_string.split()

    positions = get_position(field[0])
    if field[1] == 'w':
        turn = 1
    else:
        turn = 0

    return (positions,turn,0,0,0,0)



def change_turn(turn):
    if turn:
        turn = 0
    else:
        turn = 1
        
    return turn


# Makes the commputer make random moves
def randcomputer(board,team):
    possible_pieces = []
    pawns = []
    for square,piece_in_board in enumerate(board):
        if piece_in_board != "empty":
            if piece_in_board.team == team:
                possible_pieces.append((square,piece_in_board))

    correct = 1
    while correct == 1:
        piece_num = random.randint(0,len(possible_pieces)-1)
        piece_index = possible_pieces[piece_num][0]
        if len(possible_pieces[piece_num][1].move(piece_index,board)) != 0:
            correct = 0
    move_num = random.randint(0,len(possible_pieces[piece_num][1].move(piece_index,board))-1)
    move_index = possible_pieces[piece_num][1].move(piece_index,board)[move_num][0]

    board[move_index] = board[piece_index]
    board[piece_index] = "empty"

    for index,aa in enumerate(board):
        if aa != "empty":
            if aa.team == team:
                if aa.name == "pawn":
                    pawns.append((index,aa))
                    
    for place,ac in pawns:
        if ac.isPromotion(place):
            selection = random.randint(0,3)
            board = ac.Promotion(place,board,selection)


    return board



def piece_movement(current_cell,next_positions,board):
    
    if next_positions[1] == "normal":
        board[next_positions[0]] = board[current_cell]
        board[current_cell] = "empty"
        board[next_positions[0]].not_moved = False
        board = clean_enpassant(board)

    elif next_positions[1] == "double":
        move = next_positions[0]
        board = clean_enpassant(board)
        
        for aa in [1,-1]:
            if board[move+aa] != "empty":
                if board[move+aa].name == "pawn":
                    if move // 8 == (move + aa) // 8:
                        board[move+aa].enpassant = True
                        if board[move+aa].team:
                            if aa == 1:
                                board[move+aa].enpassant_direction = "left"
                            else:
                                board[move+aa].enpassant_direction = "right"
                        else:
                            if aa == -1:
                                board[move+aa].enpassant_direction = "left"
                            else:
                                board[move+aa].enpassant_direction = "right"


        board[move] = board[current_cell]
        board[current_cell] = "empty"
        board[move].not_moved = False

    elif next_positions[1] == "castle":
        if board[current_cell].team:
            if next_positions[0] == 58:
                board[59] = board[56]
                board[56] = "empty"
            else:
                board[61] = board[63]
                board[63] = "empty"
        else:
            if next_positions[0] == 2:
                board[3] = board[0]
                board[0] = "empty"
            else:
                board[5] = board[7]
                board[7] = "empty"

        board[next_positions[0]] = board[current_cell]
        board[current_cell] = "empty"
        board[next_positions[0]].not_moved = False
        board = clean_enpassant(board)
        
    elif next_positions[1] == "enpassant":
        board[next_positions[0]] = board[current_cell]
        board[current_cell] = "empty"
        board[next_positions[0]].not_moved = False

        if board[next_positions[0]].team:
            board[next_positions[0]+8] = "empty" 
        else:
            board[next_positions[0]-8] = "empty"
            
        board = clean_enpassant(board)

    return board
    

def clean_enpassant(board):
    for aa in board:
        if aa != "empty":
            if aa.name == "pawn":
                aa.enpassant = False
                aa.enpassant_direction = ""
    
    return board


def all_moves(team,board):

    all_moves = []
    for index,aa in enumerate(board):
        if aa != "empty":
            if aa.team != team:
                for ab in aa.movement(index,board):
                    all_moves.append(ab)
        
    return all_moves

def all_moves_check(team,board):

    all_moves = []
    for index,aa in enumerate(board):
        if aa != "empty":
            if aa.team != team:
                for ab in aa.move(index,board):
                    all_moves.append(ab)
        
    return all_moves