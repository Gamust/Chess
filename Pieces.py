import check

class Pieces:
    def __init__(self,team):
        # team is 0 = black, 1 = white
        self.team = team
        

class Rook(Pieces):
    def __init__(self, team):
        super().__init__(team)
        self.name = "rook"
        self.not_moved = True

    def move(self,current_cell,board):
        moves = check.checks(board,current_cell)
        return moves

    def movement(self,current_cell,current_board):
        moves = []
        fila, columna = current_cell//8, current_cell % 8
        for aa in [-1,0,1]:
            for bb in [-1,0,1]:
                if aa == bb or aa + bb == 0:
                    continue
                x = fila + aa
                y = columna + bb
                while 0 <= x < 8 and 0 <= y < 8:
                    if current_board[x * 8 + y] != "empty" and current_board[x * 8 + y] != current_board[current_cell]:
                        if current_board[x * 8 + y].team != self.team:
                            moves.append(((x * 8 + y), "normal"))
                            break
                        else:
                            break
                    else:
                        if current_board[x * 8 + y] == "empty":
                            moves.append(((x * 8 + y), "normal"))
                    x += aa
                    y += bb
        return moves


class Knight(Pieces):
    def __init__(self, team):
        super().__init__(team)
        self.name = "knight"
        self.not_moved = True

    def move(self,current_cell,board):
        moves = check.checks(board,current_cell)
        return moves

    def movement(self,current_cell,current_board):
        moves = []
        fila, columna = current_cell//8, current_cell % 8
        for aa,bb in [(1,2),(2,1),(-1,2),(1,-2),(-2,1),(2,-1),(-1,-2),(-2,-1)]:
            x = fila + aa
            y = columna + bb
            for _ in range(1):
                if 0 <= x < 8 and 0 <= y < 8:
                    if current_board[x * 8 + y] != "empty" and current_board[x * 8 + y] != current_board[current_cell]:
                        if current_board[x * 8 + y].team != self.team:
                            moves.append(((x * 8 + y), "normal"))
                            break
                        else:
                            break
                    else:
                        if current_board[x * 8 + y] == "empty":
                            moves.append(((x * 8 + y), "normal"))
        return moves


class Bishop(Pieces):
    def __init__(self, team):
        super().__init__(team)
        self.name = "bishop"
        self.not_moved = True

    def move(self,current_cell,board):
        moves = check.checks(board,current_cell)
        return moves

    def movement(self, current_cell,current_board):
        moves = []
        fila, columna = current_cell//8, current_cell % 8
        for aa,bb in [(1,1),(-1,1),(1,-1),(-1,-1)]:
            x = fila + aa
            y = columna + bb
            while 0 <= x < 8 and 0 <= y < 8:
                if current_board[x * 8 + y] != "empty" and current_board[x * 8 + y] != current_board[current_cell]:
                    if current_board[x * 8 + y].team != self.team:
                        moves.append(((x * 8 + y), "normal"))
                        break
                    else:
                        break
                else:
                    moves.append(((x * 8 + y), "normal"))
                x += aa
                y += bb
        return moves



class King(Pieces):
    def __init__(self, team):
        super().__init__(team)
        self.name = "king"
        self.not_moved = True

    def move(self,current_cell,board):
        moves = check.checks(board,current_cell)
        return moves

    def movement(self,current_cell, current_board):
        moves = []
        fila, columna = current_cell//8, current_cell % 8

        
        for aa in [-1,0,1]:
            for bb in [-1,0,1]:
                if aa == 0 and bb == 0:
                    continue
                x = fila + aa
                y = columna + bb
                for _ in range(1):
                    if 0 <= x < 8 and 0 <= y < 8:
                        if current_board[x * 8 + y] != "empty" and current_board[x * 8 + y] != current_board[current_cell]:
                            if current_board[x * 8 + y].team != self.team:
                                moves.append(((x * 8 + y), "normal"))
                                break
                            else:
                                break
                        else:
                            moves.append(((x * 8 + y), "normal"))

        can_castle = self._canCastle(current_cell,current_board)

        if can_castle[0]:
            if self.team:
                moves.append((58,"castle"))
            else:
                moves.append((2,"castle"))
        
        if can_castle[1]:
            if self.team:
                moves.append((62,"castle"))
            else:
                moves.append((6,"castle"))
        

        return moves
    

    def _canCastle(self,current_cell, board):

        can_castle = [False,False] # LONG CASTLE, SHORT CASTLE

        if self.not_moved:
            #short castle
            short_castle_tiles = []
            for aa in board[current_cell+1:current_cell+3]:
                if aa != "empty":
                    short_castle_tiles.append("oops")
            if current_cell + 3 < 64:
                if board[current_cell+3] != "empty":
                    if board[current_cell+3].name == "rook":
                        if board[current_cell+3].team == self.team:
                            if board[current_cell+3].not_moved:
                                if len(short_castle_tiles) == 0:
                                    can_castle[1] = True
                                else:
                                    can_castle[1] = False
            #long castle
            long_castle_tiles = []
            for aa in board[current_cell-3:current_cell]:
                if aa != "empty":
                    long_castle_tiles.append("oops")
            if current_cell - 4 >= 0:
                if board[current_cell - 4] != "empty":
                    if board[current_cell - 4].name == "rook":
                        if board[current_cell - 4].team == self.team:
                            if board[current_cell - 4].not_moved:
                                if len(long_castle_tiles) == 0:
                                    can_castle[0] = True
                                else:
                                    can_castle[0] = False


        return can_castle



class Queen(Pieces):
    def __init__(self, team):
        super().__init__(team)
        self.name = "queen"
        self.not_moved = True

    def move(self,current_cell,board):
        moves = check.checks(board,current_cell)
        return moves
        
    def movement(self,current_cell, current_board):
        moves = []
        fila, columna = current_cell//8, current_cell % 8
        for aa in [-1,0,1]:
            for bb in [-1,0,1]:
                if aa == 0 and bb == 0:
                    continue
                x = fila + aa
                y = columna + bb
                while 0 <= x < 8 and 0 <= y < 8:
                    if current_board[x * 8 + y] != "empty" and current_board[x * 8 + y] != current_board[current_cell]:
                        if current_board[x * 8 + y].team != self.team:
                            moves.append(((x * 8 + y), "normal"))
                            break
                        else:
                            break
                    else:
                        moves.append(((x * 8 + y), "normal"))
                    x += aa
                    y += bb
        return moves


class Pawn(Pieces):
    def __init__(self, team):
        super().__init__(team)
        self.name = "pawn"
        self.not_moved = True
        self.enpassant = False
        self.enpassant_direction = ""
            
    def move(self,current_cell,board):
        moves = check.checks(board,current_cell)
        return moves

    def movement(self,current_cell,current_board):
        row = current_cell//8
        moves = []
        if self.team:
            direction = -1
        else:
            direction = 1
        #down by 1
        if current_cell+(8*direction) < 64 and current_board[current_cell+(8*direction)] != "empty":
            pass
        else:
            if (current_cell//8 - (current_cell+(8*direction))//8) in [1,-1] and current_cell+(8*direction) < 64:
                moves.append((current_cell+(8*direction), "normal"))
        #take left
        if  current_cell+(7*direction) < 64 and current_board[current_cell+(7*direction)] != "empty":
            if current_board[current_cell+(7*direction)].team != self.team:
                if (current_cell//8 - (current_cell+(7*direction))//8) in [1,-1] and current_cell+(7*direction) < 64:
                    moves.append((current_cell+(7*direction), "normal"))
            
        #take right
        if  current_cell+(9*direction) < 64 and current_board[current_cell+(9*direction)] != "empty":
            if current_board[current_cell+(9*direction)].team != self.team:
                if (current_cell//8 - (current_cell+(9*direction))//8) in [1,-1] and current_cell+(9*direction) < 64:
                    moves.append((current_cell+(9*direction), "normal"))

        # two squares first moves
        if self.team:
            if row == 6:
                if current_board[current_cell+(8*direction)] == "empty":
                    if current_board[current_cell+(16*direction)] == "empty":
                        moves.append((current_cell+(16*direction), "double"))
        else:
            if row == 1:
                if current_board[current_cell+8*direction] == "empty":
                    if current_board[current_cell+(16*direction)] == "empty":
                        moves.append((current_cell+(16*direction), "double"))

        # IMPLEMENTATION EN-PASSANT

        if self.enpassant:
            if self.enpassant_direction == "right":
                moves.append(((current_cell+(7*direction)),"enpassant"))
            elif self.enpassant_direction == "left":
                moves.append(((current_cell+(9*direction)),"enpassant"))
        

        return moves

    def isPromotion(self, current_pos):
        if self.team:
            if current_pos//8 == 0:
                return True
            else:
                return False
        else:
            if current_pos//8 == 7:
                return True
            else:
                return False

    def Promotion(self, current_pos, current_board, selection):
        if selection == 0:
            knight = Knight(self.team)
            current_board[current_pos] = knight
            return current_board
        elif selection == 1:
            bishop = Bishop(self.team)
            current_board[current_pos] = bishop
            return current_board
        elif selection == 2:
            rook = Rook(self.team)
            current_board[current_pos] = rook
            return current_board
        elif selection == 3:
            queen = Queen(self.team)
            current_board[current_pos] = queen
            return current_board