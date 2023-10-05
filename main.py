import pygame
from sys import exit
import functions
import time
import check

pygame.init()

# SIZE
WIDTH = 1200
HEIGHT = 800
PADDING = 20

BOARD_WIDTH = ((2/3)*WIDTH) - (PADDING*2)
BOARD_HEIGHT = HEIGHT  - (PADDING*2)

TILE = (BOARD_WIDTH/8, BOARD_HEIGHT/8)
size = BOARD_WIDTH/8

IMAGE_SIZE = TILE

WIDTH_PROMOTION = ((WIDTH-BOARD_WIDTH)/2 - size)/2
PROMOTION_PADDING = 30


# COLORS
BROWN = (100, 50, 0)
LIGHT_BROWN = (255, 200, 150)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TURQUOISE = (175,238,238)
GOLD = (218,165,32)


# Setup the screen and FPS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Python")
Clock = pygame.time.Clock()


# Get the board in the middle of the screen
board = pygame.Surface((BOARD_WIDTH,BOARD_HEIGHT))
board_rect = board.get_rect(center = (WIDTH/2,HEIGHT/2))


# Set the tiles to draw
white_tile = pygame.Surface(TILE)
white_tile.fill(BROWN)
black_tile = pygame.Surface(TILE)
black_tile.fill(LIGHT_BROWN)

highlight = pygame.Surface(TILE)
highlight.fill(TURQUOISE)

promotion_tile = pygame.Surface(TILE)
promotion_tile.fill(GOLD)

cleaning = pygame.Surface(((WIDTH-BOARD_WIDTH)/2,HEIGHT))
cleaning.fill(BLACK)


# INSERT CHESS PIECES
bpawn = pygame.image.load("Chess/Pieces/BPawn.png").convert_alpha()
bpawn = pygame.transform.scale(bpawn,IMAGE_SIZE)
wpawn = pygame.image.load("Chess/Pieces/WPawn.png").convert_alpha()
wpawn = pygame.transform.scale(wpawn,IMAGE_SIZE)
brook = pygame.image.load("Chess/Pieces/BRook.png").convert_alpha()
brook = pygame.transform.scale(brook,IMAGE_SIZE)
wrook = pygame.image.load("Chess/Pieces/WRook.png").convert_alpha()
wrook = pygame.transform.scale(wrook,IMAGE_SIZE)
bking = pygame.image.load("Chess/Pieces/BKing.png").convert_alpha()
bking = pygame.transform.scale(bking,IMAGE_SIZE)
wking = pygame.image.load("Chess/Pieces/WKing.png").convert_alpha()
wking = pygame.transform.scale(wking,IMAGE_SIZE)
bqueen = pygame.image.load("Chess/Pieces/BQueen.png").convert_alpha()
bqueen = pygame.transform.scale(bqueen,IMAGE_SIZE)
wqueen = pygame.image.load("Chess/Pieces/WQueen.png").convert_alpha()
wqueen = pygame.transform.scale(wqueen,IMAGE_SIZE)
bknight = pygame.image.load("Chess/Pieces/BKnight.png").convert_alpha()
bknight = pygame.transform.scale(bknight,IMAGE_SIZE)
wknight = pygame.image.load("Chess/Pieces/WKnight.png").convert_alpha()
wknight = pygame.transform.scale(wknight,IMAGE_SIZE)
bbishop = pygame.image.load("Chess/Pieces/BBishop.png").convert_alpha()
bbishop = pygame.transform.scale(bbishop,IMAGE_SIZE)
wbishop = pygame.image.load("Chess/Pieces/WBishop.png").convert_alpha()
wbishop = pygame.transform.scale(wbishop,IMAGE_SIZE)


# Game creation
STARTING_GAME = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w QKqk - 0 0"
test_game = "8/8/8/8/q7/8/8/8 w QKqk - 0 0"
piece_pos,turno,_,_,_,_ = functions.Fen(STARTING_GAME)


flag = False
flag_promotion = False
move_check = True
temp_click_pos = ()
first_click_piece = 0
second_click_piece = 0
temp_piece = ""
promotion_list_of_tiles = []


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        

    # Creation of the board
    Cells = []
    for fila in range (int(board_rect.topleft[1]),int(board_rect.bottomright[1]),int(size)):
        for columna in range(int(board_rect.topleft[0]),int(board_rect.bottomright[0]),int(size)):
            iswhite = (columna + fila) % 2
            if iswhite:
                rect = pygame.Rect(columna,fila,size,size)
                Cells.append(rect)
                screen.blit(white_tile,(columna,fila))
            else:
                rect = pygame.Rect(columna,fila,size,size)
                Cells.append(rect)
                screen.blit(black_tile,(columna,fila))
    
    result = check.checkmate(piece_pos,turno)

    if result == 0:
        if not turno:
            functions.randcomputer(piece_pos, turno)
            turno = functions.change_turn(turno)
            time.sleep(0.5)
        

    # Mouse actions
    click, _, _ = pygame.mouse.get_pressed()
    if click:
        mouse = pygame.mouse.get_pos()
        if not flag_promotion:
            for index,zz in enumerate(Cells):
                if zz.collidepoint(mouse):
                    # Posotion of click and turn on and off highlight
                    flag = not flag
                    temp_click_pos = (zz[0],zz[1])
                    # Save the cell where the first click happened
                    if flag:
                        first_click_index = index
                    

                    #move the piece on the second click
                    if not flag:
                        if piece_pos[first_click_index] != "empty":
                            if piece_pos[first_click_index].team == turno:
                                possible_moves = [x[0] for x in piece_pos[first_click_index].move(first_click_index,piece_pos)]
                                if index in possible_moves:
                                    temp = piece_pos[first_click_index].move(first_click_index,piece_pos)
                                    place_to_move = temp[possible_moves.index(index)]
                                    piece_pos = functions.piece_movement(first_click_index,place_to_move,piece_pos)
                                    second_click_piece = index
                                    

                                    # CHECK FOR PROMOTION
                                    if piece_pos[second_click_piece] != "empty" and piece_pos[second_click_piece].name == "pawn":
                                        if piece_pos[second_click_piece].isPromotion(second_click_piece):
                                            loop = 0
                                            for aa in range(int(PADDING+size*2-PROMOTION_PADDING/2),int(PADDING+size*6+PROMOTION_PADDING/2),int(size+PROMOTION_PADDING/3)):
                                                prom_rect = pygame.Rect(WIDTH_PROMOTION,aa,size,size)
                                                promotion_list_of_tiles.append(prom_rect)
                                                screen.blit(promotion_tile,(WIDTH_PROMOTION,aa))
                                                if piece_pos[second_click_piece].team:
                                                    if loop == 0:
                                                        screen.blit(wknight,(WIDTH_PROMOTION,aa))
                                                    if loop == 1:
                                                        screen.blit(wbishop,(WIDTH_PROMOTION,aa))
                                                    if loop == 2:
                                                        screen.blit(wrook,(WIDTH_PROMOTION,aa))
                                                    if loop == 3:
                                                        screen.blit(wqueen,(WIDTH_PROMOTION,aa))
                                                else:
                                                    if loop == 0:
                                                        screen.blit(bknight,(WIDTH_PROMOTION,aa))
                                                    if loop == 1:
                                                        screen.blit(bbishop,(WIDTH_PROMOTION,aa))
                                                    if loop == 2:
                                                        screen.blit(brook,(WIDTH_PROMOTION,aa))
                                                    if loop == 3:
                                                        screen.blit(bqueen,(WIDTH_PROMOTION,aa))
                                                loop += 1
                                            flag_promotion = True
                                            continue
                                    turno = functions.change_turn(turno)
                    time.sleep(0.2)
    
        for index,zx in enumerate(promotion_list_of_tiles):
            if zx.collidepoint(mouse):
                if index == 0:
                    piece_pos = piece_pos[second_click_piece].Promotion(second_click_piece,piece_pos,0)
                    promotion_list_of_tiles = []
                    screen.blit(cleaning,(0,0))
                    flag_promotion = False
                    turno = functions.change_turn(turno)
                elif index == 1:
                    piece_pos = piece_pos[second_click_piece].Promotion(second_click_piece,piece_pos,1)
                    promotion_list_of_tiles = []
                    screen.blit(cleaning,(0,0))
                    flag_promotion = False
                    turno = functions.change_turn(turno)
                elif index == 2:
                    piece_pos = piece_pos[second_click_piece].Promotion(second_click_piece,piece_pos,2)
                    promotion_list_of_tiles = []
                    screen.blit(cleaning,(0,0))
                    flag_promotion = False
                    turno = functions.change_turn(turno)
                elif index == 3:
                    piece_pos = piece_pos[second_click_piece].Promotion(second_click_piece,piece_pos,3)
                    promotion_list_of_tiles = []
                    screen.blit(cleaning,(0,0))
                    flag_promotion = False
                    turno = functions.change_turn(turno)
    
    #highlight clicked cell
    if flag:
        if piece_pos[first_click_index] == "empty":
            pass
        else:
            movement = piece_pos[first_click_index].move(first_click_index,piece_pos)
            for at in movement:
                move_pos = (Cells[at[0]][0],Cells[at[0]][1])
                screen.blit(highlight,move_pos)
        

    
    # PRINT THE BOARD BY FEN NOTATION
    for index,af in enumerate(piece_pos):
        if af == "empty":
            continue
        elif af.name == "pawn":
            if af.team:
                screen.blit(wpawn,Cells[index])
            else:
                screen.blit(bpawn,Cells[index])
        elif af.name == "rook":
            if af.team:
                screen.blit(wrook,Cells[index])
            else:
                screen.blit(brook,Cells[index])
        elif af.name == "bishop":
            if af.team:
                screen.blit(wbishop,Cells[index])
            else:
                screen.blit(bbishop,Cells[index])
        elif af.name == "knight":
            if af.team:
                screen.blit(wknight,Cells[index])
            else:
                screen.blit(bknight,Cells[index])
        elif af.name == "queen":
            if af.team:
                screen.blit(wqueen,Cells[index])
            else:
                screen.blit(bqueen,Cells[index])
        elif af.name == "king":
            if af.team:
                screen.blit(wking,Cells[index])
            else:
                screen.blit(bking,Cells[index])

    if result == 0:
        pass
    elif result == 1:
        font = pygame.font.SysFont("Arial", 50)
        if turno:
            txtsurf = font.render("Black Won",True, WHITE)
            screen.blit(txtsurf,(975, HEIGHT / 2))
        else:
            txtsurf = font.render("White Won",True, WHITE)
            screen.blit(txtsurf,(975, HEIGHT / 2))
    elif result == 2:
        font = pygame.font.SysFont("Arial", 50)
        txtsurf = font.render("Draw",True, WHITE)
        screen.blit(txtsurf,(1000, HEIGHT / 2))


    pygame.display.flip()
    Clock.tick(60)
